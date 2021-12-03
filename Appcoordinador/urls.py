from django.urls import path
from .views import dashboard_coordinador, registro_usuarios, agregar_ficha

urlpatterns = [
    path('registro/', registro_usuarios,name='registro'),
    path('dashboard_coordinador/', dashboard_coordinador,name='dashboard_coordinador'),
    path('agregar_ficha/', agregar_ficha,name='agregar_ficha'),
]