from django.contrib import admin
from .models import User, Room, Booking, Payment, Facility, RoomFacility

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Facility)
admin.site.register(RoomFacility)
