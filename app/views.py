from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def registrationForm(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/registration')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode('utf-8'), salt=bcrypt.gensalt()).decode('utf-8')
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    request.session['name'] = user.first_name
    return redirect('/')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode('utf-8'), user.password.encode('utf-8'))):
            request.session['id'] = user.id
            return redirect('/properties')
    return redirect('/')

def logoutView(request):
    logout(request)
    return redirect('/')
