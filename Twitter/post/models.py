from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    pass
class Post(models.Model):
    content = models.TextField(max_length=180)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content