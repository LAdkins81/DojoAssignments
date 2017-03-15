from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render (request, 'form/index.html')

def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['dojolocation']
        request.session['comments'] = request.POST['comments']
        return render (request, 'form/result.html')
    else:
        return redirect('/')

def result(request):
    return render (request, 'form/result.html')
