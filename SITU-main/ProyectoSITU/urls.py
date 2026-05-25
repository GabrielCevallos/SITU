"""ProyectoSITU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appSITUweb.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    
    # Pasajeros URLs
    path('pasajeros/', pasajeros, name='pasajeros'),
    path('pasajerosEdit/<int:id>', pasajerosEdit, name='pasajerosEdit'),
    path('pasajerosDelete/<int:id>', pasajerosDelete, name='pasajerosDelete'),
    path('pasajerosCreate/', pasajerosCreate, name='pasajerosCreate'),
    
    # Buses URLs
    path('buses/', buses, name='buses'),
    path('busesCreate/', busesCreate, name='busesCreate'),
    path('busesEdit/<int:id>', busesEdit, name='busesEdit'),
    path('busesDelete/<int:id>', busesDelete, name='busesDelete'),
    
    # Viajes URLs
    path('viajes/', viajes, name='viajes'),
    path('viajesCreate/', viajesCreate, name='viajesCreate'),
    path('viajesEdit/<int:id>', viajesEdit, name='viajesEdit'),
    path('viajesDelete/<int:id>', viajesDelete, name='viajesDelete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
