from django.urls import path
from .views import signIn, signUp, logout, profile, likedTweets, retweets

urlpatterns = [
    path('login/',signIn, name ='signin'),
    path('register/',signUp, name = 'signup'),
    path('logout/',logout, name = 'logout'),
    path('profile/', profile, name= 'profile'),
    path('likes/', likedTweets, name= 'likedTweets'),
    path('retweet/', retweets, name= 'retweets')
]