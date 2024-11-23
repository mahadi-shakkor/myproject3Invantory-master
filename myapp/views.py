from django.shortcuts import render
from .forms import UserFormsignup

def signup(request):
    user_data = None  # Initialize user data as None

    if request.method == 'POST':
        form = UserFormsignup(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            user_data = {
                'id': user.userid,  # Get the user's unique ID from the AutoField
                'name': user.name,
                'email': user.email
            }
            return render(request, 'signup.html', {'form': form, 'user_data': user_data})
    else:
        form = UserFormsignup()

    return render(request, 'signup.html', {'form': form, 'user_data': user_data})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(userid=userid)
                
                # Check if the entered password matches the stored hashed password
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid credentials.")
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


