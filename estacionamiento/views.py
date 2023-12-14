from django.shortcuts import render
from rest_framework import generics
from .models import Estacionamiento
from estacionamiento import serializer

# Create your views here.
class EstacionamientoListaApiView(generics.ListCreateAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = serializer.EstacionamientoSerializer


class EstacionamientoIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estacionamiento.objects.all()
    serializer_class = serializer.EstacionamientoSerializer