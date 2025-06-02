# reservations/admin.py
from django.contrib import admin
from .models import GroomingAppointment, VeterinaryAppointment

admin.site.register(GroomingAppointment)
admin.site.register(VeterinaryAppointment)
