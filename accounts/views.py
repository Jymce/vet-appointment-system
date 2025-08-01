from django.views.decorators.http import require_POST
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('adminpanel:admin_dashboard')  # redirect to admin page in reservations
            else:
                return redirect('reservations:user_dashboard')  # redirect regular users to user dashboard in accounts
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('accounts:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('accounts:register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('accounts:login')

    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

@require_POST
def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # replace 'login' with your login url name
