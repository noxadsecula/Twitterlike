from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    cat = models.CharField(max_length=100)
    def __str__(self):
        return self.cat

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content