from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="users_index"),
    url(r'^authenticate$', views.authenticate, name="login"),
    url(r'^success$', views.register, name="success")
]
