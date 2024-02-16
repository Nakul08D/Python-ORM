from django.db import models

# Create your models here.

class Singer(models.Model):
    name=models.CharField(max_length=20)
    lang=models.CharField(max_length=20,default=None)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE)
    song_name=models.CharField(max_length=20)
    movie = models.CharField(max_length=20)
    song_type=models.CharField(max_length=20)
    song_duration=models.CharField(max_length=20)
    
    def __str__(self):
        return self.singer.name
    
class Token(models.Model):
    token_id=models.CharField(max_length=20)
    
    def __str__(self):
        return self.token_id
    
    
class Sub_detail(models.Model):
    token=models.OneToOneField(Token,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField(max_length=40)
    city=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Song_play(models.Model):
    
    sub_name=models.ForeignKey(Sub_detail,on_delete=models.CASCADE)
    
    singer=models.ManyToManyField(Singer)
    
    def __str__(self):
        return self.sub_name.name
    
    
    