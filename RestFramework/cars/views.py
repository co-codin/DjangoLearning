from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Car

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()