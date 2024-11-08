from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Room


# Home page view - renders everything in the homepage (index.html)
def home(request):
    return render(request, "index.html")


# About page view - separate page for about
def about(request):
    return render(request, 'about.html')


# Contact page view - separate page for contact
def contact(request):
    return render(request, 'contact.html')


# Optional: If you want separate pages for features, benefits, or how it works
def features(request):
    return render(request, 'features.html')


def benefits(request):
    return render(request, 'benefits.html')


def forms(request):
    return render(request, 'forms.html')


# Signup page view - renders signup page (signup.html)
def signup(request):
    if request.method == 'POST':
        # Collecting form data
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Create new user
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')


# Login view - authenticates user and logs them in
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate and login user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('room_list')  # Redirect to rooms list page after successful login
            else:
                return HttpResponse("Invalid login details. Please try again.")  # Optional, for failed login

    else:
        form = AuthenticationForm()

    return render(request, 'forms.html', {'form': form})


# Room list view - displays a list of rooms
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

