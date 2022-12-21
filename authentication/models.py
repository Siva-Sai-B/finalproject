from django.db import models


class Sem1(models.Model):
    Student_Roll=models.IntegerField()
    Student_Name=models.CharField(max_length=20)
    Physics=models.IntegerField()
    C=models.IntegerField()
    Maths=models.IntegerField()
    Drawing=models.IntegerField()
    ES=models.IntegerField()
    



# Create your models here.
