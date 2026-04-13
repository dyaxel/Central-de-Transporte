from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Autobus)
admin.site.register(Pasajero)
admin.site.register(Ruta)
admin.site.register(Viaje)
admin.site.register(Boleto)