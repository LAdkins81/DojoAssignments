from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='courses_index'),
    url(r'^creation$', views.creation, name='course_creation'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='course_remove'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name='course_destroy')
]
