from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room, Booking, User
from datetime import datetime
from django.http import HttpResponse

# Home page view
def home(request):
    return render(request, "index.html")

# About page view
def about(request):
    return render(request, 'about.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# Features page view
def features(request):
    return render(request, 'features.html')

# Benefits page view
def benefits(request):
    return render(request, 'benefits.html')

# Forms page view
def forms(request):
    return render(request, 'forms.html')

# Signup page view
def signup(request):
    if request.method == 'POST':
        # Create a new User object manually
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another one.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            # Save the new user
            user = User.objects.create_user(username=username, name=name, email=email, password=password)
            user.save()

            messages.success(request, "Account created successfully. Please log in.")
            return redirect('myapp:my_custom_login')
    return render(request, 'signup.html')

# Login page view
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user manually with the custom User model
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('myapp:my_choose_gender')  # Use the name of the URL pattern for the room list
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'forms.html')

# Gender selection page
@login_required
def choose_gender(request):
    return render(request, 'choose_gender.html')

# Room list view (only available rooms)
@login_required
def room_list(request):
    available_rooms = Room.objects.filter(status='available')
    return render(request, 'room_list.html', {'rooms': available_rooms})

# Room details view
@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'room_detail.html', {'room': room})

# Hall rooms view
@login_required
def hall_rooms(request, hall_name):
    rooms = Room.objects.filter(hall_name=hall_name)
    return render(request, 'hall_rooms.html', {'hall_name': hall_name, 'rooms': rooms})

# Book room view
@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    if request.method == 'POST':
        # Fetching data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booking_date_str = request.POST.get('date')
        booking_time_str = request.POST.get('time')

        # Ensure that booking_date_str and booking_time_str are not None
        if not booking_date_str or not booking_time_str:
            messages.error(request, "Date and time are required.")
            return redirect('myapp:my_book_room', room_id=room.id)

        # Convert date and time from strings
        try:
            booking_date = datetime.strptime(booking_date_str, '%Y-%m-%d').date()
            booking_time = datetime.strptime(booking_time_str, '%H:%M').time()
        except ValueError:
            messages.error(request, "Invalid date or time format.")
            return redirect('myapp:my_book_room', room_id=room.id)

        # Check if the room is still available
        if room.is_available():
            # Check if there's an existing booking for the same room and time
            overlapping_booking = Booking.objects.filter(
                room=room,
                start_date=booking_date,
                start_time=booking_time
            ).exists()

            if not overlapping_booking:
                # Create a new booking
                booking = Booking(
                    room=room,
                    user=request.user,
                    start_date=booking_date,
                    start_time=booking_time,
                    name=name,
                    email=email,
                    phone=phone,
                )
                booking.save()

                # Update room status
                room.status = 'unavailable'
                room.save()

                messages.success(request, "Room booked successfully!")
                return redirect('myapp:my_room_list')
            else:
                messages.error(request, "This room is already booked for the selected date and time.")
        else:
            messages.error(request, "The room is currently unavailable.")

    return render(request, 'book_room.html', {'room': room})

# Confirm booking view
@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    return render(request, 'confirm_booking.html', {'booking': booking})

# Filter rooms based on gender selection
@login_required
def room_list(request, gender=None):
    # Filter rooms based on gender selection
    if gender == 'female':
        rooms = Room.objects.filter(hall_name__in=['Hall 1', 'Hall 2', 'Hall 3'], status='available')
    elif gender == 'male':
        rooms = Room.objects.filter(hall_name__in=['Hall 4', 'Hall 5', 'Hall 6'], status='available')
    else:
        rooms = Room.objects.filter(status='available')  # For cases where gender is not specified

    return render(request, 'room_list.html', {'rooms': rooms, 'gender': gender})

