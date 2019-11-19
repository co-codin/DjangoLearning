from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'car'

urlpatterns = [
    path('all/', CarsListView.as_view()),
    path('car/create', CarCreateView.as_view())
]
