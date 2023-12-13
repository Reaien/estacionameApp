from django.urls import path
from . import views
import requests
from rest_framework.utils import json
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect


app_name = 'web'

#metodo login comparando datos api
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #procesar los datos del formulario para comparar con el endpoint de users
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            #solicitud get al endpoint
            url = "http://127.0.0.1:8000/usuarios/users"
            response = requests.get(url)

            #manejar la respuesta del endpoint y compararlo con los datos del formulario
            data_api = response.json()
            user_existe = any(user['email'] == email and user['password'] == password for user in data_api)

            if user_existe:
                #usuario autenticado, redirigir al home y msje
                messages.success(request, "Ingresado correctamente")
                return redirect(to="/home")
            else:
                #Usuario no autenticado, mostrar mensaje de error
                form.add_error(None, "Credenciales incorrectas. Por favor, inténtalo de nuevo.")
    else:
        form = LoginForm()
    return render(request, 'web/login.html', {'form': form})
    
def home(request):
    responseComuna = requests.get('http://127.0.0.1:8000/comunas/lista').json()
    responseUser = requests.get('http://127.0.0.1:8000/usuarios/users').json()
    return render(request, 'web/home.html',{
        'responseComuna': responseComuna,
        'responseUser': responseUser,
    })

def index(request):
    return render(request, 'web/index.html')



def postUsuario(request):
    responseTipoUser = requests.get('http://127.0.0.1:8000/tiposUsuario/listar/').json()
    url = "http://127.0.0.1:8000/usuarios/crear"
    if request.method == 'POST':
        form = UsuarioForm(request.POST or None)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")
            edad = form.cleaned_data.get("edad")
            tipoUsuario = form.data.get('tipoUsuario')
            auto = form.cleaned_data.get("auto")
            estacionamiento = form.cleaned_data.get("estacionamiento")
            comuna = form.cleaned_data.get("comuna")
            print(nombre)
            print(password)
            print(email)
            print(edad)
            print(tipoUsuario)
            print(auto)
            print(estacionamiento)
            print(comuna) 
            data = {'nombre': nombre, 'password': password, 'email': email, 'edad': edad, 'auto': auto, 'estacionamiento': estacionamiento, 'comuna': comuna, 'tipo_usuario': tipoUsuario,}
            headers = {'Content-type': 'application/json', }
            response = requests.post(url, data=json.dumps(data), headers=headers)
            messages.success(request, "Usuario registrado correctamente")
            return render(request, 'web/index.html', {
                'response': response
            })
        else:
            #Usuario no autenticado, mostrar mensaje de error
            form.add_error(None, "Credenciales incorrectas. Por favor, inténtalo de nuevo.")        
    return render(request, 'web/register.html',{
        'responseTipoUser': responseTipoUser
    })       