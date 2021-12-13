from django.urls import path
from Appcoordinador import views
urlpatterns = [
    path('registro/', views.registro_usuarios,name='registro'),
    path('base_coordinador/', views.base_coordinador,name='base_coordinador'),
    path('agregar_ficha/', views.agregar_ficha,name='agregar_ficha'),
    path('agregar_instructor/', views.agregar_instructor,name='agregar_instructor'),
    path('asignacion_horario_instructor/', views.asignacion_horario_instructor,name='asignacion_horario_instructor'),
    path('visualizar_horarios_instructores/', views.visualizar_horarios_instructores,name='visualizar_horarios_instructores'),
    path('visualizar_horarios_fichas/', views.visualizar_horarios_fichas,name='visualizar_horarios_fichas'),
    path('agregar_instructor/', views.agregar_instructor,name='agregar_instructor'),
    path('deshabilitar_instructor/', views.deshabilitar_instructor,name='deshabilitar_instructor'),
    path('deshabilitar_ficha/', views.deshabilitar_ficha,name='deshabilitar_ficha'),
    path('salir/', views.salir,name="salir"),
    path('actualizar/', views.actualizar,name="actualizar"),

]