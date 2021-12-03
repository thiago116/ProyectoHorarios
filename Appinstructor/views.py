from django.shortcuts import render

# Create your views here.

def dashboard_instructor(request):
    return render(request,"dashboard_instructor.html")