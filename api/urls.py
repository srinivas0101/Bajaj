# api/urls.py
from django.urls import path
from . import views
from .views import bfhl_post, bfhl_get

urlpatterns = [
    path('api/bfhl/', bfhl_post, name='bfhl_post'),  # POST request
    path('api/bfhl/get/', bfhl_get, name='bfhl_get')
]
