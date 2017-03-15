from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("I will do this in under 10 minutes!")
