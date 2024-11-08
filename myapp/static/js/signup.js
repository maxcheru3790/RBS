// signup.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm_password').value;

        // Check if all fields are filled
        if (!username || !email || !password || !confirmPassword) {
            alert('Please fill out all fields');
            event.preventDefault();
            return;
        }

        // Check if passwords match
        if (password !== confirmPassword) {
            alert('Passwords do not match');
            event.preventDefault();
            return;
        }

        // Add further validations if needed
    });
});
