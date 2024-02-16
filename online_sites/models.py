from django.db import models

# Create your models here.

class Site(models.Model):
    site_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.site_name
    

class LoginUser(models.Model):
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField(max_length=25)
    city=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.fname

class Profile(models.Model):
    loginUser=models.OneToOneField(LoginUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    profile_img=models.ImageField(upload_to='', height_field=None, width_field=None, max_length=None,default=None)
    description=models.CharField(max_length=50)
    dob=models.DateField(auto_now=False, auto_now_add=False, default=None)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    location=models.CharField(max_length=50)
    post_img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,default=None)
    song=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    tag=models.CharField(max_length=50)
    
    def __str__(self):
        return self.profile.name
    
    
    
    