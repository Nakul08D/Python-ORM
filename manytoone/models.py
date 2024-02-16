from django.db import models

# Create your models here.

class Teacher(models.Model):
    faculty=models.CharField(max_length=20)
    
    def __str__(self):
        return self.faculty
    
    
class Student_Id(models.Model):
    student_roll_no=models.CharField(max_length=10)
    
    def __str__(self):
        return self.student_roll_no
    
    
class Student(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    roll_num=models.OneToOneField(Student_Id, on_delete=models.CASCADE)
    
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
