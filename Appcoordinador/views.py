from django.shortcuts import render
from django.http.response import HttpResponse
from Apphorarios.forms import *
# Create your views here.
def dashboard_coordinador(request):
    return render(request,"dashboard_coordinador.html")

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
    if request.method == 'POST':
        pass
    return render(request, "agregar_ficha.html")