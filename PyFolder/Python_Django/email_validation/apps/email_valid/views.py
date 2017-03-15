from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

# Create your views here.
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'email_valid/index.html')

def success(request):
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request, messages.ERROR, 'Invalid entry! Please enter a valid email address!')
        return redirect('/')
    else:
        User.objects.create(email=request.POST['email'])
        context = {
            'email' : User.objects.all(),
            'eaddress' : request.POST['email']
        }
        return render(request, 'email_valid/success.html', context)
