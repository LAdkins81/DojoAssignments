from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def login(self, postData):
        # print "Running a login function!"
        # print "If successful login occurs, maybe return {'theuser':user} where user is a user object?"
        # print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
        pass
    def register(self, postData):
        # print ("Register a user here")
        # print ("If successful, maybe return {'theuser':user} where user is a user object?")
        # print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
        pass
class User(models.Model):
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
