from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signIn(request):
    return render(request, 'index.html')

def signUp(request):
    return render(request, 'index.html')

def logout(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def likedTweets(request):
    return render(request, 'likes.html')

def retweets(request):
    return render(request, 'retweet.html')
