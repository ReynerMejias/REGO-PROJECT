from django.urls import path
from . import views

urlpatterns = [
    path('', views.Peones, name="Peones"),
    path('peon/<str:pk>', views.Peon, name="Peon"),
    path('crearpeon', views.CrearPeon, name="CrearPeon"),
    path('crearretiro/<str:pk>', views.CrearRetiro, name="CrearRetiro"),
    path('inicio', views.InicioSesion, name="Inicio"),
    path('logout', views.logoutUser, name="Logout"),
    path('cambiaractivo/<str:pk>', views.CambiarActivo, name='CambiarActivo')
]
