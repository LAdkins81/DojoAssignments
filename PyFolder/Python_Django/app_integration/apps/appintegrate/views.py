from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import UserCourse
from ..courses.models import Course
from ..loginandreg.models import User

from django.db.models import Count
# Create your views here.

def index(request):
    return redirect(reverse('courses:courses_index'))

def add_user(request):
    context = {
        'users': User.objects.all(),
        'courses': Course.objects.all(),
        'user_courses': Course.objects.annotate(Count('reg_courses'))
    }
    return render(request, 'appintegrate/index.html', context)

def add_user_course(request):
    if request.method == 'POST':
        UserCourse.objects.addUserToCourse(request.POST)
        return redirect(reverse('integration:add_user'))
