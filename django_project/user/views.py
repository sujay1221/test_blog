from django.shortcuts import render,redirect
from .forms import UserRegistraionForm
from django.contrib import messages
# Create your views here.
#login views
#signin views
#to update profile.

def signup(request):
    form = UserRegistraionForm()
    if request.method == "POST" :
        form = UserRegistraionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}!!')
            return redirect('posts')
        else :
            form = UserRegistraionForm()
    return render(request,'user/signup.html',{'form':form})
    