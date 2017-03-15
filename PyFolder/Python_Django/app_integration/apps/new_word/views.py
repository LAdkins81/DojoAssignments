from django.shortcuts import render, redirect
# Create your views here.
import random
import string

def acounter(request):

    blah = {'rand1' : ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(25)])}

    print request.session['count']

    if 'count' in request.session:
        request.session['count'] = request.session['count'] + 1
    else:
        request.session['count'] = 0

    return render(request, 'new_word/index.html', blah)
