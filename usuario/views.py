from django.shortcuts import render
from .models import *
from .serializer import UsuariosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

#get all
@api_view(['GET'])
def UsuariosLista(request):
    users = Usuario.objects.all()
    serializer = UsuariosSerializer(users, many=True)
    return Response(serializer.data)

#get por id
@api_view(['GET'])
def UsuariosDetalle(request, pk):
    users = Usuario.objects.all(id=pk)
    serializer = UsuariosSerializer(users, many=False)
    return Response(serializer.data)

#crear user
@api_view(['POST'])
def UsuariosCrear(request):
    serializer = UsuariosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

#actualizar usuarios
@api_view(['POST'])
def UsuariosActualizar(request, pk):
    usuarios = Usuario.objects.get(id=pk)
    serializer = UsuariosSerializer(instance=usuarios, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])
def UsuariosEliminar(request, pk):
    users = Usuario.objects.get(id=pk)
    users.delete()

    return Response('Eliminado')