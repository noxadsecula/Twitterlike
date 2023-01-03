from django.urls import path
from .views import *

urlpatterns = [
    path('explore/', explore, name='explore')
]