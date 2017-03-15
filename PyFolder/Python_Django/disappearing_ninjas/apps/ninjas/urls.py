from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas_color/(?P<color>\D+)$', views.ninjas_color)
]
