from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            # Login user
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        context = {}
        return render(request, 'accounts/login.html', context)


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That users name already in use')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already in use')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password
                    )

                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('/')
                    user.save()
                    messages.success(request, 'You are registered')
                    return redirect('login')
        else:
            # messages
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        context = {}
        return render(request, 'accounts/register.html', context)


def logout(request):
    context = {}
    return redirect('index')


def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)
