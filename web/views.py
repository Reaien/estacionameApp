from django.urls import path
from . import views
import requests
from rest_framework.utils import json
from django.shortcuts import render
from .forms import UsuarioForm
from django.contrib import messages

app_name = 'web'

def index(request):
    response = requests.get('http://127.0.0.1:8000/usuarios/').json()
    return render(request, 'web/usuarioAPI.html', {
        'response': response
    })

def postUsuario(request):
    url = "http://127.0.0.1:8000/usuarios/crear"
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        edad = form.cleaned_data.get("edad")
        auto = form.cleaned_data.get("auto")
        estacionamiento = form.cleaned_data.get("estacionamiento")
        comuna = form.cleaned_data.get("comuna")
        print(nombre)
        print(password)
        print(email)
        print(edad)
        print(auto)
        print(estacionamiento)
        print(comuna) 
        data = {'nombre': nombre, 'password': password, 'email': email, 'edad': edad, 'auto': auto, 'estacionamiento': estacionamiento, 'comuna': comuna}
        headers = {'Content-type': 'application/json', }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return render(request, 'web/form.html', {
            'response': response
        })
