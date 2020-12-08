from django.shortcuts import render,redirect
from .forms import UserRegistraionForm,UserUpdateForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
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
    
@login_required(login_url='login')
def profile(request):
    if request.method=='POST' :
        u_form =  UserUpdateForm(request.POST or None,instance = request.user)
        p_form = ProfileForm(request.POST or None,request.FILES,instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account has been updated!')
            return redirect('posts')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'user/profile.html',context)