from django.db import models
from django.contrib.auth.models import User


class user(User):
    profile_pic = models.ImageField(upload_to='static/images/profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
