from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail, send_mass_mail # plan to use mass mail later.

from travel_world import settings
# Create your views here.

def home(request):
    return render(request, 'travelers/index.html')

# blog, contact, services, about

def blog(request):
    return render(request, 'travelers/blog.html')
def contact(request):
    return render(request, 'travelers/contact.html')
def services(request):
    return render(request, 'travelers/services.html')
def about(request):
    return render(request, 'travelers/about.html')

def giving(request, pk):
    return HttpResponseRedirect(reverse('travelers:index', args=(pk,)))

def signup(request):
    return render(request, 'travelers/signup.html')

def signup_check(request):
    if request.method == 'POST':

        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        password_confirmation = request.POST['password_confirmation'].strip()
        first_name = request.POST['firstname'].strip()
        last_name = request.POST['lastname'].strip()

        if not (username and email and password and password_confirmation and first_name and last_name):
            messages.error(request, 'Please fill all the fields')
            return redirect('travelers:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('travelers:signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('travelers:signup')

        if password != password_confirmation:
            messages.error(request, 'Passwords do not match')
            return redirect('travelers:signup')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'Invalid email')
            return redirect('travelers:signup')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True
        user.save()

        # welcome email
        subject = 'Welcome to Travelers World'
        message = f'Hello {user.username}!\nWelcome to Travelers World.\nThank you for considering us.\nPlease check your email {user.email} to confirm your registration.\nThank you.\n- Raihan Rony'

        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        messages.success(request, 'Account created successfully')
        return HttpResponseRedirect(reverse('travelers:signup'))

    return render(request, 'travelers/signup.html')

def check_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password) 
            return  user
        else:
            messages.error(request, 'Invalid Credentials')
    return  None

def signin(request):
    return render(request, 'travelers/signin.html')

def signin_check(request):
   
    user = check_user(request)
    
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('travelers:home'))
    else:
        return redirect('travelers:login')

@login_required
def profile(request):
    
    user = request.user

    if user.is_superuser:
        return redirect( '/admin/')
    elif user.is_staff:
        return render(request, 'travelers/profile.html')
    else :
        return render(request, 'travelers/profile.html')
        
   