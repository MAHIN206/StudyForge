from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Subject


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


@login_required(login_url='login')
def dashboard(request):

    subjects = Subject.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'subjects': subjects
    })


@login_required(login_url='login')
def subjects(request):

    subjects = Subject.objects.filter(user=request.user)

    return render(request, 'subjects.html', {
        'subjects': subjects
    })


@login_required(login_url='login')
def create_subject(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')

        if name:
            Subject.objects.create(
                user=request.user,
                name=name,
                description=description
            )

            return redirect('subjects')

    return render(request, 'create_subject.html')


def user_logout(request):
    logout(request)
    return redirect('home')