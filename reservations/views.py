from django.shortcuts import render,redirect, get_object_or_404

from reservations.models import VeterinaryAppointment,GroomingAppointment
from .forms import GroomingAppointmentForm, VeterinaryAppointmentForm

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required


def dashboard(request):
    return render(request, 'reservations/dashboard.html')

# Decorator to allow only superusers
def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func

@superuser_required
def admin_dashboard(request):
    return render(request, 'reservations/admin_dashboard.html')

@login_required
def services(request):
    return render(request, 'reservations/services.html')

@login_required
def grooming(request):
    # Implement your grooming service form or page here
    return render(request, 'reservations/grooming.html')

@login_required
def veterinary(request):
    # Implement your veterinary service form or page here
    return render(request, 'reservations/veterinary.html')

@login_required
def grooming_appointment_view(request):
    if request.method == 'POST':
        form = GroomingAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user  # set the logged-in user as owner
            appointment.save()
            return redirect('reservations:services')  # or success page
    else:
        form = GroomingAppointmentForm()

    return render(request, 'reservations/grooming_form.html', {'form': form})



@login_required
def veterinary_appointment_view(request):
    if request.method == 'POST':
        form = VeterinaryAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.owner = request.user  # set the logged-in user as owner
            appointment.save()
            return redirect('reservations:services')  # or your preferred success page
    else:
        form = VeterinaryAppointmentForm()

    return render(request, 'reservations/veterinary_form.html', {'form': form})


@login_required
def user_appointments(request):
    grooming_appointments = GroomingAppointment.objects.filter(owner=request.user)
    veterinary_appointments = VeterinaryAppointment.objects.filter(owner=request.user)

    return render(request, 'reservations/user_appointments.html', {
        'grooming_appointments': grooming_appointments,
        'veterinary_appointments': veterinary_appointments,
    })


@login_required
def grooming_detail(request, pk):
    appointment = get_object_or_404(GroomingAppointment, id=pk, owner=request.user)
    return render(request, 'reservations/grooming_detail.html', {'appointment': appointment})
@login_required
def veterinary_detail(request, pk):
    appointment = get_object_or_404(VeterinaryAppointment, pk=pk, owner=request.user)
    return render(request, 'reservations/veterinary_detail.html', {'appointment': appointment})

@login_required
def cancel_grooming(request, pk):
    appointment = get_object_or_404(GroomingAppointment, pk=pk, owner=request.user)
    if request.method == "POST" and appointment.status == "Pending":
        appointment.status = "Canceled"
        appointment.save()
    return redirect('reservations:user_appointments')
    

@login_required
def cancel_veterinary(request, pk):
    appointment = get_object_or_404(VeterinaryAppointment, pk=pk, owner=request.user)
    if request.method == "POST" and appointment.status == "Pending":
        appointment.status = "Canceled"
        appointment.save()
    return redirect('reservations:user_appointments')
