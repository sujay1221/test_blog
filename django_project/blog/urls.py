from django.contrib import admin
from blog import views
from django.urls import path,include



urlpatterns = [
    path('about/',views.about,name='about'),
    path('blog/',views.blog.as_view(),name="posts"),
    path('<str:pk>/home/',views.user_blog,name="user-home")

]