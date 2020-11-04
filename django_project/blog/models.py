from django.db import models
from django.contrib.auth.models import User

class blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    images = models.ImageField(upload_to='static/images/blog_img')

    def __str__(self):
        return (self.title + " by " + "author")

    class Meta:
        ordering = ['-date_posted']