from django.urls import path
from .views import visualizar_horarios

urlpatterns = [
    path('visualizar_horarios/', visualizar_horarios,name='visualizar_horarios'),
]