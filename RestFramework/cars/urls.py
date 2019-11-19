from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'car'

urlpatterns = [
    path('car/create', CarCreateView.as_view())
]
