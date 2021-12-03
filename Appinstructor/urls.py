from django.urls import path
from .views import dashboard_instructor

urlpatterns = [
    path('dashboard_instructor/', dashboard_instructor,name='dashboard_instructor'),
]