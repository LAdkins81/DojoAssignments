from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render (request, 'ninjas/index.html')

def ninjas(request):
    return render (request, 'ninjas/ninjas.html')

def ninjas_color(request, color):
    verify = True
    context = {
        'routecolor' : color,
        'key' : verify,
        'blue' : 'blue',
        'red' : 'red',
        'purple' : 'purple',
        'orange' : 'orange'
    }
    return render(request, 'ninjas/ninjas.html', context)
