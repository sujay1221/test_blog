from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from blog.models import blog
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .filters import BlogFilter

def about(request):
   return render(request,'blog/about.html',{})



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



class Blog(generic.ListView):
    model = blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-date_posted']
    paginate_by = 4


class BlogDetailView(generic.DetailView):
    model = blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'


class BlogCreateView(LoginRequiredMixin,generic.CreateView):
    model = blog
    fields = ['title','content','image1','image2','pdf','company_name','salary']
    template_name = 'blog/blog_form.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = blog
    fields = ['title','content','image1','image2','pdf','company_name','salary']
    template_name = 'blog/blog_form.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model = blog    
    template_name = 'blog/blog_delete.html'
    success_url = '/blog/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def Filter(request):
    b = blog.objects.all()
    myfilter = BlogFilter(request.GET,queryset=b)
    blogs = myfilter.qs
    context = { 'myfilter':myfilter, 'blogs':blogs}
    return render(request,'blog/blog_filter.html',context)






#views yet to create  .......
#blog views ------------------------------------------loads all blog listview genric view
#home views ------------------------------------------loads all blog releated to user.
#blog views create a basic page.


