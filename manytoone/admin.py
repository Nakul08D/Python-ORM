from django.contrib import admin
from manytoone.models import Teacher,Student_Id,Student

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student_Id)
admin.site.register(Student)