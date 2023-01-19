from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('catalog/', catalogURLregen, name='catRegen'),
    path('catalog/<path:catalogPath>/', catalog, name='catalog'),
    path('pa/', personalAccount, name='PA'),
    path('auth/', auth, name='auth'),
]