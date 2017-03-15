from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^user_courses$', add_user, name='add_user'),
    url(r'^add_user_course$', add_user_course, name='add_user_course')
]
