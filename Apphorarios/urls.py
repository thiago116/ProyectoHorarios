from django.urls import path,include
from .views import  login_view, logout_view

urlpatterns = [
    path('login/',login_view,name="login" ),
    path('coordinador/', include('Appcoordinador.urls'),name="coordinador"),
    path('instructor/', include('Appinstructor.urls'),name="instructor"),
    path('logout/',logout_view,name="logout"),
]

