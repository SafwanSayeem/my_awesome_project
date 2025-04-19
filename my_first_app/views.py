from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Define BASE_DIR as the root of the project (assuming views.py is in an app folder)
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = BASE_DIR / '.env'
load_dotenv(dotenv_path)  # Load environment variables from the .env file

# Print the API key for development/debugging (you can remove this in production)
print(f"HF_API_KEY from env: {os.getenv('HF_API_KEY')}")

def summarize_text(request):
    summary = None
    
    if request.method == "POST":
        text = request.POST.get("text")

        if not text:
            summary = "Please enter text to summarize."
        else:
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY')}"}

            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": text})
                
                if response.status_code == 200:
                    summary = response.json()[0]['summary_text']
                elif response.status_code == 503:
                    summary = "API is overloaded. Please try again in 1-2 minutes."
                else:
                    print(f"Error: {response.status_code}, Response: {response.text}")
                    summary = f"Error (HTTP {response.status_code}): Something went wrong."

            except Exception as e:
                summary = f"Connection failed: {str(e)}"

    return render(request, "summarize.html", {"summary": summary})
