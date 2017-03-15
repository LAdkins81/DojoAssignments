from django.shortcuts import render
import time
import datetime

#CONTROLLER!!!!
#create your views here.
def index(request):
    time = {
        'datetime': datetime.datetime.now().strftime("It's %A! Month: %m Day: %d Year: %y, and it's %H:%M %p")
            }
    return render(request, 'timedisplay/index.html', time)

# def show(request):
#     print(request.method)
#     return render(request, 'timedisplay/show_users.html')
