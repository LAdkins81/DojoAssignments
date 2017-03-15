from __future__ import unicode_literals

from django.db import models

# Create your models here.
import bcrypt

class UserManager(models.Manager):
    def login(self, email, password):
        user = User.objects.get(email=email)
        pw = password
        hashed = bcrypt.hashpw(pw.encode(), user.password.encode())
        if user.password == hashed:
            return {'msg' : 'Yay! You have logged in successfully, ', 'name' : user.first_name, 'id': user.id}
        else:
            return None

    def register(self, info):
        pw = info['password']
        hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        User.objects.create(first_name=info['first_name'], last_name=info['last_name'], email=info['email'], password=hashed)
        return {'msg' : 'success: you have registered!'}

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=100)
    confirmpass = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
