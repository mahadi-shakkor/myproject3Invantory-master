from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password, make_password
from .forms import UserFormsignup, LoginForm
from .models import User  # Ensure your models are imported correctly

# Signup View
def signup(request):
    """
    Handles user signup. Validates the form data, hashes the password,
    and saves the user to the database.
    """
    user_data = None  # Initialize user data for displaying after signup

    if request.method == 'POST':
        form = UserFormsignup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save yet, to hash the password
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user to the database
            
            # Prepare user data for display after successful signup
            user_data = {
                'id': user.userid,  # Get the user's unique ID from AutoField
                'name': user.name,
                'email': user.email
            }
            return render(request, 'signup.html', {'form': form, 'user_data': user_data})
    else:
        form = UserFormsignup()  # Create a blank form for GET request

    return render(request, 'signup.html', {'form': form, 'user_data': user_data})


# Login View
def login_view(request):
    """
    Handles user login. Validates the form data and checks credentials
    against the database. Logs the user in if credentials are valid.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userid = form.cleaned_data['userid']
            password = form.cleaned_data['password']

            try:
                # Fetch user by userid
                user = User.objects.get(userid=userid)
                print("Entered Password:", password)  # Debugging step
                print("Stored Hashed Password:", user.password)  # Debugging step

                # Check if entered password matches the stored hashed password
                if check_password(password, user.password):
                    print("Password matched!")  # Debugging step
                    login(request, user)  # Log the user in
                    return redirect('home')  # Redirect to the home page
                else:
                    print("Password did not match!")  # Debugging step
                    messages.error(request, "Invalid credentials.")  # Display error message
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials.")  # User not found
    else:
        form = LoginForm()  # Create a blank form for GET request

    return render(request, 'login.html', {'form': form})
