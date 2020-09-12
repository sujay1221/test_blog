from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blog.models import blog

def about(request):
    return HttpResponse('About page.')
    

class blog(generic.ListView):
    model = blog
    template_name = '/blog/blog.html'
    context_object_name = 'blogs'
    







#views yet to create  .......
#blog views ------------------------------------------loads all blog listview genric view
#home views ------------------------------------------loads all blog releated to user.
#blog views create a basic page.


