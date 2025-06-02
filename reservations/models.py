from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Canceled', 'Canceled'),
]

class GroomingAppointment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50, choices=[('Dog', 'Dog'), ('Cat', 'Cat')])
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    contact_number = models.CharField(max_length=15)
    grooming_package = models.CharField(
        max_length=100,
        choices=[
            ('Basic Bath', 'Basic Bath'),
            ('Full Groom', 'Full Groom'),
            ('Nail Trim', 'Nail Trim'),
            ('Ear Cleaning', 'Ear Cleaning'),
        ]
    )
    add_ons = models.CharField(max_length=255, blank=True)
    coat_type = models.CharField(max_length=100)
    behavior_notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # ✅ NEW
    notes = models.TextField(blank=True, null=True)
    reminder_sent = models.BooleanField(default=False)


    def __str__(self):
        return f"Grooming for {self.pet_name} on {self.preferred_date}"


class VeterinaryAppointment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50, choices=[('Dog', 'Dog'), ('Cat', 'Cat')])
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    contact_number = models.CharField(max_length=15)
    visit_type = models.CharField(
        max_length=100,
        choices=[
            ('Check-up', 'Check-up'),
            ('Vaccination', 'Vaccination'),
            ('Illness', 'Illness'),
            ('Surgery', 'Surgery'),
            ('Emergency', 'Emergency'),
        ]
    )
    symptoms = models.TextField()
    current_medications = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # ✅ NEW
    notes = models.TextField(blank=True, null=True)
    reminder_sent = models.BooleanField(default=False)



    def __str__(self):
        return f"Vet visit for {self.pet_name} on {self.preferred_date}"
