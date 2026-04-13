"""
URL configuration for Transportes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', cerrar_sesion,name='logout'),
    path('', inicio,name='inicio'),
    path('registro/', registro, name='registro'),
    path('visualizacion/', visualizacion, name='visualizacion'),
    path('registrar_bus/', registrar_bus, name='registrar_bus'),
    path('registrar_ruta/', registrar_ruta, name='registrar_ruta'),
    path('registrar_viaje/', registrar_viaje, name='registrar_viaje'),
    path('registrar_pasajero/', registrar_pasajero, name='registrar_pasajero'),
    path('ver_viajes/', ver_viajes, name='ver_viajes'),
    path('comprar_boleto/<int:viaje_id>/', comprar_boleto, name='comprar_boleto'),
    path('nuevo_usuario/', nuevo_usuario, name='nuevo_usuario'),
    path('mis_boletos', mis_boletos, name='mis_boletos'),
]
