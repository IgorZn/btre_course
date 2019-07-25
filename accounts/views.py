from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)


def logout(request):
    context = {}
    return redirect('index')


def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
