# send_reminders.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from datetime import timedelta
from reservations.models import GroomingAppointment, VeterinaryAppointment

class Command(BaseCommand):
    help = 'Send email reminders for upcoming appointments'

    def handle(self, *args, **kwargs):
        tomorrow = timezone.localdate() + timedelta(days=1)

        grooming_appointments = GroomingAppointment.objects.filter(
            preferred_date=tomorrow,
            status='Approved',
            reminder_sent=False
        )

        veterinary_appointments = VeterinaryAppointment.objects.filter(
            preferred_date=tomorrow,
            status='Approved',
            reminder_sent=False
        )

        for appt in grooming_appointments:
            self.send_email(appt.owner.email, appt.owner.get_full_name(), appt.pet_name, appt.preferred_date, appt.preferred_time, 'Grooming')
            appt.reminder_sent = True
            print(f"Sent reminder to {appt.owner.email} for {appt.pet_name} on {appt.preferred_date} at {appt.preferred_time}")
            appt.save()

        for appt in veterinary_appointments:
            self.send_email(appt.owner.email, appt.owner.get_full_name(), appt.pet_name, appt.preferred_date, appt.preferred_time, 'Veterinary')
            appt.reminder_sent = True
            print(f"Sent reminder to {appt.owner.email} for {appt.pet_name} on {appt.preferred_date} at {appt.preferred_time}")
            appt.save()

        if not grooming_appointments and not veterinary_appointments:
            print("No reminders to send today.")


    def send_email(self, to_email, owner_name, pet_name, date, time, type):
        formatted_time = time.strftime('%I:%M %p')  # Convert to 12-hour format
        subject = f"Reminder: {type} Appointment for {pet_name} Tomorrow"
        message = (
            f"Hello {owner_name},\n\n"
            f"This is a friendly reminder that your {type.lower()} appointment for {pet_name} is scheduled for tomorrow, {date} at {formatted_time}.\n\n"
            "Thank you for booking with us!"
        )
        from_email = 'your-email@gmail.com'
        send_mail(subject, message, from_email, [to_email])
