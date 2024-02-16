from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name=models.CharField( max_length=20)

    def __str__(self):
        return self.brand_name
    
class Color(models.Model):
    color_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.color_name
    
    
class Product(models.Model):
    brand=models.ManyToManyField(Brand)
    
    name=models.CharField(max_length=20)
    
    color=models.ManyToManyField(Color)
    
    def __str__(self):
        return self.name
    
    


