import django
from apps.third_app.models import *

django.setup()

all_people = People.objects.all()
for p in all_people:
    print p.first_name, p.last_name
