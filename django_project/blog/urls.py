from django.contrib import admin
from blog import views
from django.urls import path,include

app_name = 'blog'

urlpatterns = [
    path('about/',views.about,name='about'),
]