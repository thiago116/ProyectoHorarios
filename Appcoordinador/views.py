from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from Apphorarios.forms import *
from Apphorarios.views import logout_view
from .forms import *
# Create your views here.

def registro_usuarios(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("datos guardados")
        else:
            return HttpResponse("formulario invalido")
    else:
        form = SignUpForm()
        
    return render(request,"registro_usuarios.html",{'forms':form})

def agregar_ficha(request):
    print(request.POST)
    if request.method == 'POST':
        
        form = AddFichas(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponse("datos guardados")
        else:
            return HttpResponse("vuelva a llenar el formulario")
    else:
        form = AddFichas()
    return render(request, "agregar_ficha.html",{'form':form})

def base_coordinador(request):
    return render(request,"base_coordinador.html")

def agregar_instructor(request):
    if request.method == 'POST':
        form = AddInstructores(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("se agregó correctamente")
        else:
            return HttpResponse("hay un error")
    else:
        form = AddInstructores()
    return render(request,"agregar_instructor.html",{'form':form})

def asignacion_horario_instructor(request):
    return render(request,"asignar_horario_instructor.html")

def visualizar_horarios_instructores(request):
    return render(request,"visualizar_horarios_instructores.html")

def visualizar_horarios_fichas(request):
    return render(request,"visualizar_horarios_fichas.html")

def deshabilitar_ficha(request):
    return render(request,"deshabilitar_ficha.html")

def deshabilitar_instructor(request):
    return render(request,"deshabilitar_instructor.html")

def salir(request):
    logout_view(request)
    messages.success(request,F"Tu sesion se ha cerrado correctamente")
    return redirect("login")

