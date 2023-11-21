# Create your views here.
from django.shortcuts import render
from .models import *
from .serializer import ComunaSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Create your views here.

#get all
class ComunaLista(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


@api_view(['GET'])
def ComunasAll(request):
    comunas = Comuna.objects.all()
    serializer = ComunaSerializer(comunas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def ComunasActualizar(request, pk):
    comunas = Comuna.objects.get(id=pk)
    serializer = ComunaSerializer(instance=comunas, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
def ComunaEliminar(request, pk):
    comunas = Comuna.objects.get(id=pk)
    comunas.delete()

    return Response('Eliminado')