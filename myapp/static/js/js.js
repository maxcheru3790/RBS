document.addEventListener('DOMContentLoaded', function () {
    // Example: Handle form submission for room booking
    const bookingForm = document.getElementById('booking-form'); // The form ID

    if (bookingForm) {
        bookingForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the form from submitting normally

            // Get the user input values from the form
            const room = document.getElementById('room').value; // Room input field
            const date = document.getElementById('date').value; // Date input field
            const time = document.getElementById('time').value; // Time input field

            // Basic validation to ensure all fields are filled
            if (!room || !date || !time) {
                alert('Please fill in all the fields');
                return;
            }

            // Show confirmation message
            const confirmationMessage = `
                Your room booking has been confirmed:
                Room: ${room}
                Date: ${date}
                Time: ${time}
            `;
            alert(confirmationMessage);
        });
    }

    // Dynamically populate room options in the dropdown
    const roomsDropdown = document.getElementById('room');
    const availableRooms = ['Meeting Room 1', 'Conference Room', 'Event Hall', 'Classroom'];

    availableRooms.forEach(function(room) {
        const option = document.createElement('option');
        option.value = room;
        option.textContent = room;
        roomsDropdown.appendChild(option);
    });
});
