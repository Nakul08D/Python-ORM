from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.base,name='base'),
    path('index/',views.index,name='index'),
    path('site/',views.site,name='site'),
    path('user/<int:id>/',views.userlist,name='usersite'),
]
