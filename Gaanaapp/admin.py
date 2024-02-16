from django.contrib import admin
from Gaanaapp.models import Singer,Song,Token,Sub_detail,Song_play

# Register your models here.

@admin.register(Song)   
class SongAdmin(admin.ModelAdmin):
    list_display=['singer','song_name','movie','song_type','song_duration']
    
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['name','lang']
    
@admin.register(Sub_detail)   
class Sub_detailAdmin(admin.ModelAdmin):
    list_display=['token','name','number','email','city']
    
@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display=['token_id']
    
@admin.register(Song_play)
class Song_playAdmin(admin.ModelAdmin):
    list_display=['sub_name','get_singer']
    
    def get_singer(self,instance):
        return  [tag.name for tag in instance.singer.all()]