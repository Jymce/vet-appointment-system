from django.urls import path
from . import views
app_name = 'reservations'

urlpatterns = [
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('services/', views.services, name='services'),
    path('services/grooming/', views.grooming, name='grooming'),
    path('services/veterinary/', views.veterinary, name='veterinary'),
    path('grooming/', views.grooming_appointment_view, name='grooming'),
    path('veterinary/', views.veterinary_appointment_view, name='veterinary'),

    path('appointments/', views.user_appointments, name='user_appointments'),
    path('grooming/<int:pk>/', views.grooming_detail, name='grooming_detail'),
    path('veterinary/<int:pk>/', views.veterinary_detail, name='veterinary_detail'),
    path('cancel/grooming/<int:pk>/', views.cancel_grooming, name='cancel_grooming'),
    path('cancel/veterinary/<int:pk>/', views.cancel_veterinary, name='cancel_veterinary'),

    path('settings/', views.account_settings, name='account_settings'),


]
