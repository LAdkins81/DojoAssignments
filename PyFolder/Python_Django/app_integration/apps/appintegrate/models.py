from __future__ import unicode_literals

from django.db import models
from ..courses.models import Course
from ..loginandreg.models import User
from django.db.models import Count
# Create your models here.

class UserCourseManager(models.Manager):
    def addUserToCourse(self, object):
        user_id = object['users']
        user = User.objects.get(id=user_id)
        course_id = object['courses']
        course = Course.objects.get(id=course_id)
        UserCourse.objects.create(user_id=user, course_id=course)
        return {'success' : 'User added to course'}

class UserCourse(models.Model):
    user_id = models.ForeignKey(User, null=True, related_name="reg_users")
    course_id = models.ForeignKey(Course, related_name="reg_courses")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserCourseManager()
