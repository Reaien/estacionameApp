from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('login', views.index, name='login'),
    path('form', views.postUsuario, name='formulario'),
    path('home', views.home, name='home')

]
