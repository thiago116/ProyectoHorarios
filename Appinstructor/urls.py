from django.urls import path
from Appinstructor import views

urlpatterns = [
    path('visualizar_horarios/', views.visualizar_horarios,name='visualizar_horarios'),
    path('salir/', views.salir,name="salir"),
]