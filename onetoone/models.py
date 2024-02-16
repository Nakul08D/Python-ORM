from django.db import models

# Create your models here.

class Student_Id(models.Model):
    student_id=models.CharField(max_length=10)

    def __str__(self):
        return self.student_id
    
class Student_detail(models.Model):
    student=models.OneToOneField(Student_Id, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    city=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
