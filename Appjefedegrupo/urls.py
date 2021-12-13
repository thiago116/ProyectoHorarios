from django.urls import path
from Appjefedegrupo import views

urlpatterns = [
    path('visualizar_horarios_trimestres/', views.visualizar_horarios_trimestres,name='visualizar_horarios_trimestres'),
    path('salir/', views.salir,name="salir"),
]