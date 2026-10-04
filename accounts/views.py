from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password.'
            })

    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
def user_logout(request):
    logout(request)
    return redirect('home')