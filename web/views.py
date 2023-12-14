import requests
from rest_framework.utils import json
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm, EstacionamientoForm
from django.contrib import messages


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
            # usuario autenticado, obtener información completa del usuario
            user = next((u for u in data_api if u['email'] == email and u['password'] == password), None)
            if user:
                #pasar datos del user al redirect 
                request.session['user_data'] = user
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
    #obtener el dato de sesión desde el redirect
    user_data = request.session.get('user_data', None)
    responseComuna = requests.get('http://127.0.0.1:8000/comunas/lista').json()
    postEstacionamiento = 'http://127.0.0.1:8000/estacionamientos/listar/'
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            nombreContacto = form.cleaned_data.get("nombreContacto")
            fonoContacto = form.cleaned_data.get("fonoContacto")
            comuna = form.data.get("nombreComuna")
            direccion = form.cleaned_data.get("direccion")
            imagenEstacionamiento = form.files.get("imagenEstacionamiento")
            archivos = {'imagenEstacionamiento': (imagenEstacionamiento.name, imagenEstacionamiento.file)}
            data = {'nombreContacto': nombreContacto, 'fonoContacto': fonoContacto, 'nombreComuna': comuna, 'direccion': direccion}
            requests.post(postEstacionamiento, data=data, files=archivos)
            messages.success(request, "Estacionamiento registrado correctamente")
            return redirect(to='/home')
        else:
            form.add_error(None, "Credenciales incorrectas. Por favor, inténtalo de nuevo.")
    return render(request, 'web/home.html',{
        'responseComuna': responseComuna,
        'user_data': user_data,
    })

def index(request):
    return render(request, 'web/index.html')

def admin_users(request):
    responseUser = requests.get("http://127.0.0.1:8000/usuarios/users").json()
    return render(request, 'web/admin_users.html',{
        'responseUser': responseUser
    })

#eliminar usuario admin
def eliminar_usuario(request, id):
    # Enviar solicitud DELETE a la API
    url = f'http://127.0.0.1:8000/usuarios/detalle/{id}'
    requests.delete(url)
    messages.success(request, "Usuario eliminado correctamente")
    return redirect(to='/admin_users')

def admin_est(request):
    responseEst = requests.get("http://127.0.0.1:8000/estacionamientos/listar/").json()
    return render(request, 'web/admin_est.html',{
        'responseEst': responseEst
    })


#importante explicar filtro por id con api
def estComuna(request, id):
    responseComuna = requests.get(f'http://127.0.0.1:8000/comunas/detalle/{id}').json()
    responseEstacionamiento = requests.get('http://127.0.0.1:8000/estacionamientos/listar/').json()
    estacionamientos_filtrados = [est for est in responseEstacionamiento if est['nombreComuna'] == responseComuna['nombreComuna']]
    return render(request, 'web/est_comuna.html',{
        'responseComuna': responseComuna,
        'responseEstacionamiento': estacionamientos_filtrados,
    })



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
            comuna = form.cleaned_data.get("comuna")
            data = {'nombre': nombre, 'password': password, 'email': email, 'edad': edad, 'tipo_usuario': tipoUsuario, 'comuna': comuna, }
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
        'responseTipoUser': responseTipoUser,
    })       