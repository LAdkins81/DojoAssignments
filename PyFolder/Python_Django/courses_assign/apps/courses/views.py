from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        'courseinfo' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def creation(request):
    Course.objects.create(name = request.POST['name'], description=request.POST['descrip'])
    return redirect('/')

def remove(request, id):
    courseinfo = Course.objects.get(id=id)
    context = {
        'courseid' : id,
        'courseinfo' : Course.objects.filter(id=id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
