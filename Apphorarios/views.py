from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def base_coordinador(request):
    return render(request,"base_coordinador.html")

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_coordinador:
                login(request,user)
                return redirect('base_coordinador')
            if user is not None and user.is_instructor:
                login(request,user)
                return redirect('visualizar_horarios')
            if user is not None and user.is_JGrupo:
                login(request,user)
                return redirect('dashboardjg')
            else:
                return HttpResponse("credenciales incorrectas")
        else:
            return HttpResponse("error validando los campos")
    return render(request,"login.html",{'forms':form})
def logout_view(request):
    logout(request)
    return redirect('login')