from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render (request, 'ninjagold/index.html')

def play(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            request.session['gold'] = random.randrange(10,21)
        elif request.POST['building'] == 'cave':
            request.session['gold'] = random.randrange(5,11)
        elif request.POST['building'] == 'house':
            request.session['gold'] = random.randrange(2,6)
        elif request.POST['building'] == 'casino':
            request.session['gold'] = random.randrange(-50,51)
        if request.session["gold"] > 0:
            request.session["activities"].insert(0, "Earned " + str(request.session["gold"]) + " golds from the " + request.POST['building'] + "!")
        else:
            request.session["activities"].insert(0, "Entered a casino and lost " + str(-request.session["gold"]) + " golds... Ouch...")
        request.session['count'] = request.session['count'] + request.session['gold']
        return redirect('/')
