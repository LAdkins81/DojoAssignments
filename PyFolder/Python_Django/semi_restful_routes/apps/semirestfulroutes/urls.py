from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^products$', views.index),
    url(r'^products/(?P<id>\d+)$', views.show),
    url(r'^products/new/$', views.new),
    url(r'^products/create$', views.create),
    url(r'^products/(?P<id>\d+)/edit$', views.edit),
    url(r'^products/(?P<id>\d+)/update$', views.update),
    url(r'^products/(?P<id>\d+)/destroy$', views.destroy)
]
