from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image1 = models.ImageField(upload_to='static/images/blog_img',null=True)
    image2 = models.ImageField(upload_to='static/images/blog_img',null=True)
    company_name = models.CharField(max_length=30,null=True)
    salary_range = [('4','4lakh'),('6','6lakh'),('8','8lakh'),('10','10lakh'),('12','12lakh'),('14','14lakh'),('16','16lakh'),('20','20lakh'),('30','30lakh'),('35','35lakh'),('40','40lakh')]
    salary = models.CharField(max_length=3,choices=salary_range,null=True)
    pdf = models.FileField(upload_to='static/files',null=True)

    def __str__(self):
        return (self.title + " by " + "author" + self.author.username)

    class Meta:
        ordering = ['-date_posted']

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    