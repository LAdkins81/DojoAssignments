from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authenticate$', views.authenticate),
    url(r'^success$', views.register),
    url(r'^logout$', views.logout)
]
