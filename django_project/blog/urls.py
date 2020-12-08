from django.contrib import admin
from blog import views
from django.urls import path,include



urlpatterns = [
    path('about/',views.about,name='about'),
    path('blog/',views.Blog.as_view(),name="posts"),
    path('home/<int:pk>/',views.user_blog,name="user-home"),
    path('post/<int:pk>/',views.BlogDetailView.as_view(),name="post-detail"),
    path('post/new/',views.BlogCreateView.as_view(),name="blog-create"),
    path('post/<int:pk>/update/',views.BlogUpdateView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',views.BlogDeleteView.as_view(),name="post-delete"),
    path('post/filter/',views.Filter,name="post-filter"),
]