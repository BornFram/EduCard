from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('catalog/<path:catalogPath>/', catalog, name='catalog'),

    path('pa/', personalAccount, name='PA'),
    path('auth/', auth, name='auth'),
]