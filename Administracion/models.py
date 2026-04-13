from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Autobus (models.Model):
    placa = models.CharField(primary_key=True, max_length=8)
    capacidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.placa}"

class Pasajero (models.Model):
    dpi = models.CharField(primary_key=True, max_length=13)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200)
    
    def __str__(self):
        return f"{self.nombre} - {self.dpi}"

class Ruta (models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.origen} -> {self.destino}"

class Viaje (models.Model):
    fecha_y_hora = models.DateTimeField()
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    bus = models.ForeignKey(Autobus, on_delete=models.CASCADE)
        
    class Meta:
        unique_together = ('bus', 'fecha_y_hora')
    
    def __str__(self):
        return f"{self.ruta} - {self.fecha_y_hora}"

class Boleto (models.Model):
    numero_asiento = models.IntegerField(primary_key=True)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    
    class Meta:
        unique_together = ('viaje', 'numero_asiento')
    
    def __str__(self):
        return f"{self.viaje} - {self.numero_asiento}"
    
    
"""     def clean(self):
        if not self.viaje:
            return

        if self.numero_asiento > self.viaje.bus.capacidad:
            raise ValidationError("Asiento fuera de capacidad")

        boletos_vendidos = Boleto.objects.filter(viaje=self.viaje).count()
        if boletos_vendidos >= self.viaje.bus.capacidad:
            raise ValidationError("No hay asientos disponibles") """