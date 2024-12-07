// JavaScript function to filter rooms by gender
function filterRooms(gender) {
    const rooms = document.querySelectorAll('.room');
    const genderHalls = {
        female: ['Hall 1', 'Hall 2', 'Hall 3'],
        male: ['Hall 4', 'Hall 5', 'Hall 6']
    };

    if (!genderHalls[gender]) {
        console.error(`Invalid gender selected: ${gender}`);
        return; // Exit if the gender is invalid
    }

    let visibleRooms = 0; // Counter to track visible rooms

    rooms.forEach(room => {
        const hallName = room.getAttribute('data-hall');
        if (genderHalls[gender].includes(hallName)) {
            room.style.display = 'block'; // Show matching rooms
            visibleRooms++;
        } else {
            room.style.display = 'none'; // Hide non-matching rooms
        }
    });

    // Provide feedback if no rooms are available
    const roomList = document.querySelector('.room-list');
    if (visibleRooms === 0 && roomList) {
        roomList.innerHTML = `<p>No rooms available for the selected gender.</p>`;
    }
}

// JavaScript function to handle room booking
function bookRoom(roomId) {
    if (!roomId) {
        console.error('Invalid room ID for booking.');
        return; // Exit if roomId is not provided
    }
    window.location.href = `/book/${roomId}`;
}
