from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    context = {
        'myproducts' : Product.objects.all()
    }
    return render(request, 'semirestfulroutes/index.html', context)

def new(request):
    return render(request, 'semirestfulroutes/newproduct.html')

def create(request):
    if request.method == 'POST':
        Product.objects.newprod(request.POST)
    return redirect('/')

def show(request, id):
    context = {
    'productinfo' : Product.objects.filter(id=id)
    }
    return render(request, 'semirestfulroutes/productdisplay.html', context)

def edit(request, id):
    context = {
    'productinfo' : Product.objects.filter(id=id)
    }
    return render(request, 'semirestfulroutes/editproduct.html', context)

def update(request, id):
    if request.method == 'POST':
        Product.objects.updateprod(request.POST, id)
    return redirect('/')

def destroy(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('/')
