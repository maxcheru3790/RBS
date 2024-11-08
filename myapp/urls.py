from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('', views.home, name='my_index'),  # Home page
    path('about/', views.about, name='my_about'),  # About page
    path('contact/', views.contact, name='my_contact'),  # Contact page
    path('benefits/', views.benefits, name='my_benefits'),  # Benefits page
    path('features/', views.features, name='my_features'),  # Features page
    path('forms/', views.forms, name='my_forms'),  # Forms page
    path('signup/', views.signup, name='my_signup'),  # Signup page
    path('rooms/', views.room_list, name='room_list'),  # Room list page

    # Custom login page
    path('login/', views.custom_login, name='login'),  # Use custom login view
]
