from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasajeroFormulario, BusFormulario, ViajeFormulario
from .models import Pasajero, Bus, Viaje

# ==================== HOME ====================
def home_view(request):
    return render(request,"index.html",{})

# ==================== PASAJEROS CRUD ====================
def pasajeros(request):
    data = PasajeroFormulario()    
    pasajeros = Pasajero.objects.all()
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

    return render(request,"pasajeros.html",{"pasajeros":pasajeros, 'form':data})

def pasajerosEdit(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    data = {
        'form': PasajeroFormulario(instance=pasajero)
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, instance=pasajero, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")

    return render(request,'pasajerosEdit.html',data)

def pasajerosDelete(request, id):
    pasajero = get_object_or_404(Pasajero, id=id)
    pasajero.delete()
    return redirect(to="pasajeros")

def pasajerosCreate(request):
    data = {
        'form': PasajeroFormulario()
    }
    if request.method == 'POST':
        formulario = PasajeroFormulario(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="pasajeros")
    return render(request, 'agregar.html', data)

# ==================== BUSES CRUD ====================
def buses(request):
    buses = Bus.objects.all()
    data = {'buses': buses}
    return render(request, "buses.html", data)

def busesCreate(request):
    data = {
        'form': BusFormulario()
    }
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="buses")
    return render(request, 'agregarBus.html', data)

def busesEdit(request, id):
    bus = get_object_or_404(Bus, id=id)
    data = {
        'form': BusFormulario(instance=bus)
    }
    if request.method == 'POST':
        formulario = BusFormulario(data=request.POST, instance=bus)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="buses")

    return render(request, 'editarBus.html', data)

def busesDelete(request, id):
    bus = get_object_or_404(Bus, id=id)
    bus.delete()
    return redirect(to="buses")

# ==================== VIAJES CRUD ====================
def viajes(request):
    viajes = Viaje.objects.all()
    data = {'viajes': viajes}
    return render(request, "viajes.html", data)

def viajesCreate(request):
    data = {
        'form': ViajeFormulario()
    }
    if request.method == 'POST':
        formulario = ViajeFormulario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="viajes")
    return render(request, 'agregarViaje.html', data)

def viajesEdit(request, id):
    viaje = get_object_or_404(Viaje, id=id)
    data = {
        'form': ViajeFormulario(instance=viaje)
    }
    if request.method == 'POST':
        formulario = ViajeFormulario(data=request.POST, instance=viaje)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="viajes")

    return render(request, 'editarViaje.html', data)

def viajesDelete(request, id):
    viaje = get_object_or_404(Viaje, id=id)
    viaje.delete()
    return redirect(to="viajes")