from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
# Create your views here.
def index(request):
    return render(request, 'loginandreg/index.html')

def authenticate(request):
    context = {
    'successlogin' : User.objects.login(request.POST['logemail'], request.POST['logpass'])
    }
    return render(request, 'loginandreg/success.html', context)

def register(request):
    error_switch = False

    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request, messages.ERROR, 'Invalid entry! Please enter a valid email address!')
        error_switch = True

    if len(request.POST['first_name']) < 2:
        messages.add_message(request, messages.ERROR, 'First name must be longer than 2 letters.')
        error_switch = True
    elif not NAME_REGEX.match(request.POST['first_name']):
        messages.add_message(request, messages.ERROR, 'First name must contain only letters.')
        error_switch = True

    if len(request.POST['last_name']) < 2:
        messages.add_message(request, messages.ERROR, 'Last name must be longer than 2 letters.')
        error_switch = True
    elif not NAME_REGEX.match(request.POST['last_name']):
        messages.add_message(request, messages.ERROR, 'Last name must contain only letters.')
        error_switch = True

    if len(request.POST['password']) < 8:
        messages.add_message(request, messages.ERROR, 'Password must be longer than 8 characters.')
        error_switch = True

    if request.POST['confirmpass'] != request.POST['password']:
        messages.add_message(request, messages.ERROR, 'Passwords must match.')
        error_switch = True

    if error_switch == True:
        return redirect('/')

    else:
        context = {
        'successreg' : User.objects.register(request.POST)
        }
        return render(request, 'loginandreg/success.html', context)
