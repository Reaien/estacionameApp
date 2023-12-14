from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.postUsuario, name='register'),
    path('home', views.home, name='home'),
    path('estComuna/<str:id>', views.estComuna, name='estComuna'),
    path('admin_users', views.admin_users, name='admin_users'),
    path('admin_est', views.admin_est, name='admin_est'),
    path('eliminar_usuario/<id>', views.eliminar_usuario, name='eliminar_usuario'),

]
