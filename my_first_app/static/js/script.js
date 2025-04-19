document.getElementById("summarize-form").addEventListener("submit", function(e) {
    const button = document.querySelector(".btn-summarize");
    const originalText = button.textContent;
    
    // Show loading state
    button.disabled = true;
    button.textContent = "Summarizing...";
    
    // Optional: Add a spinner (requires CSS)
    button.innerHTML = `<span class="spinner"></span> Summarizing...`;
    
    // Revert after submission (if not redirecting)
    setTimeout(() => {
        button.disabled = false;
        button.textContent = originalText;
    }, 3000);
});