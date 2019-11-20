from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Car
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser, )