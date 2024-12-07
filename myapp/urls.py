from django.urls import path
from . import views  # Import views from the same app

app_name = "myapp"

urlpatterns = [
    # Home page
    path('', views.home, name='my_index'),

    # About page
    path('about/', views.about, name='my_about'),

    # Contact page
    path('contact/', views.contact, name='my_contact'),

    # Benefits page
    path('benefits/', views.benefits, name='my_benefits'),

    # Features page
    path('features/', views.features, name='my_features'),

    # Forms page
    path('forms/', views.forms, name='my_forms'),

    # Signup page
    path('signup/', views.signup, name='my_signup'),

    # Custom login page
    path('login/', views.custom_login, name='my_custom_login'),

    # Room list page (lists available rooms)
    path('rooms/', views.room_list, name='my_room_list'),

    # Room detail page for a specific room by ID
    path('rooms/<int:room_id>/', views.room_detail, name='my_room_detail'),

    # Page to book a specific room using its ID
    path('rooms/<int:room_id>/book/', views.book_room, name='my_book_room'),

    # Confirm booking page after user has filled the form
    path('bookings/<int:booking_id>/confirm/', views.confirm_booking, name='my_confirm_booking'),

    # Hall rooms view (lists rooms in a specific hall by name)
    path('halls/<str:hall_name>/', views.hall_rooms, name='my_hall_rooms'),
    path('rooms/male/', views.room_list, {'gender': 'male'}, name='my_male_rooms'),
    path('rooms/female/', views.room_list, {'gender': 'female'}, name='my_female_rooms'),
    path('rooms/<str:gender>/', views.room_list, name='my_room_list_by_gender'),
    path('gender/',views.choose_gender,name='my_choose_gender'),
]
