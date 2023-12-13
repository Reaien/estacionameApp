from django.urls import path
from tipoUsuario import views


urlpatterns=[
    path('listar/', views.TipoUsuarioListaApiView.as_view()),
    path('listar/<str:pk>/', views.TipoUsuarioIdApiView.as_view())
]