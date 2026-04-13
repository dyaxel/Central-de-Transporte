from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import * 
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from Administracion.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def visualizacion(request):
    
    autobuses = Autobus.objects.all()
    rutas = Ruta.objects.all()
    viajes = Viaje.objects.all()
    
    return render(request, 'visualizacion.html',{'autobuses':autobuses, 'rutas':rutas, 'viajes':viajes})

@login_required
def registro(request):
    
    return render(request, 'registro.html')

@login_required
def registrar_bus(request):
    
    if request.method == 'POST':
        form = AutobusForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            return redirect('visualizacion')
    else:
        form=AutobusForm()
    return render(request, 'registrar_autobus.html',{'bus_form':form})
    
@login_required
def registrar_ruta(request):
    
    if request.method == 'POST':
        form = RutaForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            return redirect('visualizacion')
    else:
        form=RutaForm()
    return render(request, 'registrar_ruta.html',{'ruta_form':form})

@login_required
def registrar_viaje(request):
    
    if request.method == 'POST':
        form = ViajeForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            return redirect('visualizacion')
    else:
        form=ViajeForm()
    return render(request, 'registrar_viaje.html',{'viaje_form':form})

@login_required
def ver_viajes(request):
    
    viajes = Viaje.objects.all()
    
    return render(request, 'ver_viajes.html',{'viajes':viajes})
    
@login_required
def registrar_pasajero(request):
    
    if request.method == 'POST':
        form = PasajeroForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('inicio')
    else:
        form = PasajeroForm()
    return render(request, 'registrar_pasajero.html',{'pasajero_form':form})

@login_required
def comprar_boleto(request, viaje_id):
    viaje = get_object_or_404(Viaje, id=viaje_id)

    if request.method == 'POST':
        form = BoletoForm(request.POST)
        
        if form.is_valid():
            datos = form.cleaned_data
            buscar = Boleto.objects.filter(numero_asiento=datos['numero_asiento'],viaje=viaje).exists()
            

            
            if not buscar:
                contar = Boleto.objects.filter(viaje=viaje).count()
                capacidad = Autobus.objects.get(placa=viaje.bus)
                
                if contar < capacidad.capacidad and datos['numero_asiento'] <= capacidad.capacidad:
                    
                
                    boleto = Boleto.objects.create(
                        numero_asiento= datos['numero_asiento'],
                        pasajero = datos['pasajero'],
                        viaje = viaje,
                        usuario = request.user
                    )
                    return redirect('mis_boletos')
            else:
                messages.error(request, 'este asiento no esta disponible')
                return redirect('comprar_boleto',viaje_id)
    else:
        form = BoletoForm()

    return render(request, 'comprar_boletos.html', {'boleto_form': form,'viaje': viaje})

@login_required
def mis_boletos(request):
    
    boletos = Boleto.objects.filter(usuario= request.user)
    
    return render(request, 'mis_boletos.html',{'boletos':boletos})








""" form = TransferenciaForm(request.POST or None)


    if form.is_valid():
        info = form.cleaned_data
        retirar = Cuenta.objects.get(numero_cuenta=info['de_cuenta'])
        depositar = Cuenta.objects.get(numero_cuenta=info['a_cuenta'])

        retiro = Transaccion.objects.create(
                cuenta = retirar,
                tipo = "retiro",
                monto = info["monto"],
                descripcion = info["descripcion"]
            )
        
        deposito = Transaccion.objects.create(
                cuenta = depositar,
                tipo = "deposito",
                monto = info["monto"],
                descripcion = info["descripcion"]
        )
        
        retirar.saldo = retirar.saldo - Decimal(info['monto'])
        retirar.save()

        depositar.saldo = depositar.saldo + Decimal(info['monto'])
        depositar.save()
        
        messages.success(request,"Transacción Exitosa")
        return redirect('realizar_transferencia')
    
    else:
        return render(request, 'transferencias.html', {'form':form}) """







def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def nuevo_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro_usuario.html', {'form': form})