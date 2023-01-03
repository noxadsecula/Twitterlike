from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserCreation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    def __str__(self):
        return self.username

class Profile(models.Model):
    tagname = models.CharField.one_to_one(User, on_delete=models.CASCADE, default=User.username)
    bio = models.CharField(max_length=200)
    image = models.ImageField()
    def __str__(self):
        return self.tagname.username

    @property
    def followers(self):
        return Follow.objects.filter(followUser=self.tagname).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.tagname).count()

    def save(self):
        super().save()

class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    followUser = models.ForeignKey(User, related_name='followUser', on_delete=models.CASCADE)
