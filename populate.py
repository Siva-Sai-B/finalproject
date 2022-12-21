import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','loginsystem.settings')
django.setup()
from authentication.models import *
from faker import Faker
from random import *
fake=Faker()
for i in range(1,65):
    Sem1.objects.get_or_create(Student_Roll=i,Student_Name=fake.name(), Physics=randint(50,100),C=randint(50,100),Maths=randint(50,100),Drawing=randint(50,100),ES=randint(50,100))
    
