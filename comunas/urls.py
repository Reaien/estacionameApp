from django.urls import path
from .import views


urlpatterns = [
    path('lista', views.ComunasAll, name="lista"),
    path('actualizar/<str:pk>/', views.ComunasActualizar, name="actualizar"),
    path('eliminar/<str:pk>/', views.ComunaEliminar, name="eliminar"),
    path('detalle/<str:pk>/', views.ComunasId.as_view(), name="detalle")

]
