from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', catalog, name='home'),
    path('pa/', personalAccount, name='PA'),
    path('auth/', auth, name='auth'),


]