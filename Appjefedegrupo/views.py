from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from Apphorarios.forms import *
from Apphorarios.views import logout_view

# Create your views here.

def visualizar_horarios_trimestres(request):
    return render(request,"visualizar_horarios_trimestres.html")

def salir(request):
    logout_view(request)
    messages.success(request,F"Tu sesion se ha cerrado correctamente")
    return redirect("login")