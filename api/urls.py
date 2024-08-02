# api/urls.py
from django.urls import path
from .views import bfhl_post, bfhl_get

urlpatterns = [
    path('bfhl', bfhl_post),
    path('bfhl', bfhl_get),
]
