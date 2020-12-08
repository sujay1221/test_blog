from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile

class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','password1','password2','email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields =  ['username','email']

    

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic','bio','sem']


