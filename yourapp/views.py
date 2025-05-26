from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserDetails

def home(request):
    return render(request, 'home.html') 

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserDetails
from django.db import IntegrityError

def signup2(request):
    if request.method == 'POST':
        username = request.POST.get('username')        
        email = request.POST.get('emailaddress')       
        password = request.POST.get('password')         

        if username and email and password:
           
            if User.objects.filter(username=username).exists():
                return render(request, 'signin.html', {'error': 'Username already exists. Please choose another.'})

            try:
                # Step 1: Create User object
                user = User.objects.create_user(username=username, email=email, password=password)

                # Step 2: Save UserDetails linked to User
                user_details = UserDetails(Name=user, Email=email, Password=password)
                user_details.save()

                return redirect('home')  # Redirect to home after successful signup

            except IntegrityError:
                return render(request, 'signin.html', {'error': 'An error occurred during registration. Please try again.'})
        else:
            return render(request, 'section/signin.html', {'error': 'All fields are required.'})

    return render(request, 'section/signin.html')

def custom_view(request):
    return render(request, 'section/signin.html') 


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')  # Replace with your actual home route name
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'section/signin.html')  # Adjust path as needed
