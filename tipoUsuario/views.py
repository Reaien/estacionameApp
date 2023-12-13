from django.shortcuts import render
from rest_framework import generics
from tipoUsuario import serializer
from .models import TipoUsuario
# Create your views here.
class TipoUsuarioListaApiView(generics.ListCreateAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = serializer.TipoUsuarioSerializer


class TipoUsuarioIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoUsuario.objects.all()
    serializer_class = serializer.TipoUsuarioSerializer