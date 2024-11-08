function handleSubmit(event) {
    event.preventDefault();

    // Simulate form submission delay
    document.getElementById("formStatus").style.display = "block";
    document.getElementById("formStatus").textContent = "Sending...";

    // Simulate success message after a delay
    setTimeout(() => {
        document.getElementById("formStatus").textContent = "Message sent successfully!";

        // Reset the form after submission
        document.getElementById("contactForm").reset();

        // Hide the status message after a few seconds
        setTimeout(() => {
            document.getElementById("formStatus").style.display = "none";
        }, 3000);
    }, 2000);

    return false;
}
