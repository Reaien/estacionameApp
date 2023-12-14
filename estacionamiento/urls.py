from django.urls import path
from estacionamiento import views

urlpatterns = [
    path('listar/', views.EstacionamientoListaApiView.as_view()),
    path('listar/<str:pk>/', views.EstacionamientoIdApiView.as_view())
]