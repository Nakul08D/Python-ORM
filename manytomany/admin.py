from django.contrib import admin
from manytomany.models import Brand,Color,Product

# Register your models here.

admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Product)