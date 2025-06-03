from django import forms
from .models import GroomingAppointment, VeterinaryAppointment
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class GroomingAppointmentForm(forms.ModelForm):
    class Meta:
        model = GroomingAppointment
        fields = [
            'pet_name', 'pet_type', 'breed', 'age',
            'preferred_date', 'preferred_time', 'contact_number',
            'grooming_package', 'add_ons', 'coat_type', 'behavior_notes'
        ]
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
            })


class VeterinaryAppointmentForm(forms.ModelForm):
    class Meta:
        model = VeterinaryAppointment
        fields = [
            'pet_name', 'pet_type', 'breed', 'age',
            'preferred_date', 'preferred_time', 'contact_number',
            'visit_type', 'symptoms', 'current_medications'
        ]
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
            })

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    pass

