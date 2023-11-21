from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('crear', views.ComunaLista,basename='comunaApi')

urlpatterns = [
    path('', include(router.urls)),
    path('lista', views.ComunasAll, name="lista"),
    path('actualizar/<str:pk>/', views.ComunasActualizar, name="actualizar"),
    path('eliminar/<str:pk>', views.ComunaEliminar, name="eliminar")

]
