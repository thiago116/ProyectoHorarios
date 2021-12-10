from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def visualizar_horarios(request):
    return render(request,"visualizar_horarios.html")