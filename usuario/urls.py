from django.urls import path
from .import views

urlpatterns = [
    path('users', views.UsuariosLista, name="index"),
    path('detalle/<str:pk>', views.UsuariosDetalle, name="detalle"),
    path('crear', views.UsuariosCrear, name="crear"),
    path('actualizar/<str:pk>/', views.UsuariosActualizar, name="actualizar"),
    path('eliminar/<str:pk>', views.UsuariosEliminar, name="eliminar"),
]
