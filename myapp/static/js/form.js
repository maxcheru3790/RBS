// login.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        // Basic validation before submitting form
        if (!email || !password) {
            alert('Please fill out all fields');
            event.preventDefault();
        }
    });
});
