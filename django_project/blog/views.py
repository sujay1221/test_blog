from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from blog.models import blog
from django.contrib.auth.models import User


def about(request):
   return render(request,'blog/about.html',{})

class blog(generic.ListView):
    model = blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

#class user_blog(generic.ListView):
#    context_object_name = 'user_blogs'
#    template_name = 'blog/user_blog.html'
#
#    def get_queryset(self):
#        User = get_object_or_404(user,username=self.kwargs.get('username'))
#        return blog.objects.filter(author=User).order_by('-date_posted')

def user_blog(request,pk):
    author = User.objects.get(id=pk)
    user_blog = blog.objects.filter(author=author)
    return render(request,'blog/user_blog.html',{'user_blog':user_blog})






#views yet to create  .......
#blog views ------------------------------------------loads all blog listview genric view
#home views ------------------------------------------loads all blog releated to user.
#blog views create a basic page.


