from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from datetime import date

# User model: Represents a system user (Admin, Guest)
class User(models.Model):
    username = models.CharField(max_length=100, unique=True, default='default_username')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # Defining possible roles for the user
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('guest', 'Guest')
    ]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='guest')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def set_password(self, raw_password):
        """Hash and save the password."""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """Check if the provided password matches the stored hashed password."""
        return check_password(raw_password, self.password)

    def is_admin(self):
        """Return True if the user is an admin, False otherwise."""
        return self.role == 'admin'

    class Meta:
        ordering = ['-created_at']


# Room model: Represents rooms in a hotel, with various attributes like type and status
class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ]
    room_name = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=6, choices=ROOM_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    ]
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='available')
    hall_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.room_name

    def is_available(self):
        """Check if the room is available."""
        return self.status == 'available'

    class Meta:
        ordering = ['room_name']


# Booking model: Represents a booking of a room by a user
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, db_index=True)
    start_date = models.DateField()
    end_date = models.DateField()

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled')
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='pending', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.name}"

    def is_active(self):
        """Check if the booking is active."""
        return self.status == 'confirmed' and date.today() <= self.end_date

    def cancel_booking(self):
        """Cancel the booking."""
        self.status = 'canceled'
        self.save()

    def save(self, *args, **kwargs):
        """Ensure that end_date is after start_date."""
        if self.start_date > self.end_date:
            raise ValueError("End date must be after start date")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('room', 'start_date', 'end_date')


# Payment model: Represents a payment made for a booking
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('mpesa', 'M-Pesa'),
        ('credit_card', 'Credit Card'),
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('paypal', 'PayPal')
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, db_index=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, default='mpesa')  # Added payment method
    mpesa_transaction_id = models.CharField(max_length=255, blank=True, null=True)  # M-Pesa transaction reference

    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed')
    ]
    payment_status = models.CharField(max_length=7, choices=PAYMENT_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Payment {self.id} for booking {self.booking.id}"

    def mark_as_paid(self):
        """Mark the payment as paid."""
        self.payment_status = 'paid'
        self.save()

    def mark_as_failed(self):
        """Mark the payment as failed."""
        self.payment_status = 'failed'
        self.save()

    class Meta:
        ordering = ['-payment_date']


# Facility model: Represents various facilities available in rooms
class Facility(models.Model):
    facility_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.facility_name

    class Meta:
        ordering = ['facility_name']


# RoomFacility model: Represents the many-to-many relationship between rooms and facilities
class RoomFacility(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('room', 'facility')
        ordering = ['room', 'facility']

    def __str__(self):
        return f"{self.room.room_name} - {self.facility.facility_name}"

