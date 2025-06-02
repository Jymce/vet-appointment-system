from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    # Dashboard
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # User Management
    path('manage-account/', views.manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),

    # Appointment Reservations
    path('reservations/', views.admin_reservations, name='admin_reservations'),

    # Appointment Actions (Accept / Cancel)
    path('reservations/<str:appointment_type>/<int:pk>/accept/', views.admin_accept_appointment, name='admin_accept_appointment'),
    path('reservations/<str:appointment_type>/<int:pk>/cancel/', views.admin_cancel_appointment, name='admin_cancel_appointment'),

    # Detail views for appointments
    path('reservations/grooming/<int:pk>/', views.grooming_appointment_detail, name='grooming_appointment_detail'),
    path('reservations/veterinary/<int:pk>/', views.veterinary_appointment_detail, name='veterinary_appointment_detail'),


    #Update Status
    path('update_status/<str:type>/<int:pk>/<str:action>/', views.update_status, name='update_status'),

]
