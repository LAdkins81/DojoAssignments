from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("I hope I get it in under 5!")
