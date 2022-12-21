from django.contrib import admin
from authentication.models import *
class Sem1admin(admin.ModelAdmin):
    list_display=['Student_Name']
admin.site.register(Sem1,Sem1admin)

# Register your models here.
