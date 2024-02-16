from django.contrib import admin
from online_sites.models import Site,LoginUser,Profile,Post

# Register your models here.
@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display=['id','site_name','username']
    
    def username(self,instance):
        li = LoginUser.objects.filter(site_id=instance.id)
        
        return [i.fname for i in li ]
    
@admin.register(LoginUser)
class LoginUserAdmin(admin.ModelAdmin):
    list_display=['fname','lname','number','email','city','get_site']
    
    def get_site(self,instance):
        return instance.site.site_name
    
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','description','dob']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['location','song','description','tag']

