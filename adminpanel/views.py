from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from .decorators import superuser_required
from django.contrib.admin.views.decorators import staff_member_required

from reservations.models import GroomingAppointment, VeterinaryAppointment


@superuser_required
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')


@superuser_required
def manage_users(request):
    users = User.objects.filter(is_superuser=False)
    return render(request, 'adminpanel/manage_account.html', {'users': users})


@superuser_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if username and email:
            user.username = username
            user.email = email

            if password:
                user.set_password(password)  # properly hashes the password

            user.save()
            messages.success(request, 'User updated successfully.')
            return redirect('adminpanel:manage_users')
        else:
            messages.error(request, 'Username and email are required.')

    return render(request, 'adminpanel/edit_user.html', {'user': user})


@superuser_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('adminpanel:manage_users')
    return render(request, 'adminpanel/delete_user.html', {'user': user})


@staff_member_required
def admin_reservations(request):
    appointment_type = request.GET.get('type', 'all')
    appointment_status = request.GET.get('status', 'all')

    # Base querysets
    grooming_qs = GroomingAppointment.objects.all()
    veterinary_qs = VeterinaryAppointment.objects.all()

    # Filter by status
    if appointment_status != 'all':
        grooming_qs = grooming_qs.filter(status=appointment_status)
        veterinary_qs = veterinary_qs.filter(status=appointment_status)

    # Filter by type
    if appointment_type == 'grooming':
        grooming_appointments = grooming_qs
        veterinary_appointments = VeterinaryAppointment.objects.none()
    elif appointment_type == 'veterinary':
        grooming_appointments = GroomingAppointment.objects.none()
        veterinary_appointments = veterinary_qs
    else:  # all
        grooming_appointments = grooming_qs
        veterinary_appointments = veterinary_qs

    context = {
        'appointment_type': appointment_type,
        'appointment_status': appointment_status,
        'grooming_appointments': grooming_appointments,
        'veterinary_appointments': veterinary_appointments,
        # other context variables...
    }
    return render(request, 'adminpanel/admin_reservations.html', context)


@staff_member_required
def admin_accept_appointment(request, type, pk):
    if type == 'grooming':
        appt = get_object_or_404(GroomingAppointment, pk=pk)
    elif type == 'veterinary':
        appt = get_object_or_404(VeterinaryAppointment, pk=pk)
    else:
        messages.error(request, 'Invalid appointment type.')
        return redirect('adminpanel:admin_reservations')

    if appt.status == 'Pending':
        appt.status = 'Approved'
        appt.save()
        messages.success(request, f'{type.capitalize()} appointment approved.')
    else:
        messages.warning(request, 'Appointment is not pending.')

    return redirect('adminpanel:admin_reservations')


@staff_member_required
def admin_cancel_appointment(request, type, pk):
    if type == 'grooming':
        appt = get_object_or_404(GroomingAppointment, pk=pk)
    elif type == 'veterinary':
        appt = get_object_or_404(VeterinaryAppointment, pk=pk)
    else:
        messages.error(request, 'Invalid appointment type.')
        return redirect('adminpanel:admin_reservations')

    if appt.status == 'Pending':
        appt.status = 'Canceled'
        appt.save()
        messages.success(request, f'{type.capitalize()} appointment canceled.')
    else:
        messages.warning(request, 'Appointment is not pending.')

    return redirect('adminpanel:admin_reservations')


def grooming_appointment_detail(request, pk):
    appointment = get_object_or_404(GroomingAppointment, pk=pk)

    if request.method == 'POST':
        appointment.preferred_date = request.POST.get('preferred_date')
        appointment.preferred_time = request.POST.get('preferred_time')
        appointment.save()
        return redirect('adminpanel:grooming_appointment_detail', pk=appointment.pk)

    return render(request, 'adminpanel/grooming_appointment_detail.html', {
        'appointment': appointment
    })

@staff_member_required
def veterinary_appointment_detail(request, pk):
    appointment = get_object_or_404(VeterinaryAppointment, pk=pk)

    if request.method == 'POST':
        appointment.preferred_date = request.POST.get('preferred_date')
        appointment.preferred_time = request.POST.get('preferred_time')
        appointment.save()
        return redirect('adminpanel:veterinary_appointment_detail', pk=appointment.pk)

    return render(request, 'adminpanel/veterinary_appointment_detail.html', {'appointment': appointment})


@require_POST
def update_status(request, type, pk, action):
    # Decide which model to use
    if type == 'grooming':
        Model = GroomingAppointment
    elif type == 'veterinary':
        Model = VeterinaryAppointment
    else:
        return JsonResponse({'error': 'Invalid type'}, status=400)

    try:
        appointment = Model.objects.get(pk=pk)
    except Model.DoesNotExist:
        return JsonResponse({'error': 'Appointment not found'}, status=404)

    # Update status
    if action == 'approve':
        appointment.status = 'Approved'
    elif action == 'cancel':
        appointment.status = 'Canceled'
    else:
        return JsonResponse({'error': 'Invalid action'}, status=400)

    appointment.save()
    return JsonResponse({'success': True})
