from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',null=True)
    bio = models.TextField(blank=True,null=True)
    sem_list = [('1','first'),('2','second'),('3','third'),('4','fourth'),('5','fifth'),('6','sixth'),('7','seventh'),('8','eigth')]
    sem = models.CharField(max_length=1,choices=sem_list,default='first')



    def __str__(self):
        return self.user.username
