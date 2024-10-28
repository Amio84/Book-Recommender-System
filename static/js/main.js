// Form Validation
function validateForm() {
    const bookName = document.getElementById('bookName').value;
    const feedback = document.getElementById('searchFeedback');
    if (!bookName.trim()) {
        feedback.style.display = 'block';
        return false;
    }
    feedback.style.display = 'none';
    return true;
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});


