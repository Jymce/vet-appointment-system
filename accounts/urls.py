from django.urls import path
from django.contrib.auth import views as auth_views

from django.views.decorators.http import require_POST
from . import views
from .views import logout_view

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='user_dashboard'),

    path('logout/', logout_view, name='logout'),


]