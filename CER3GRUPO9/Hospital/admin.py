from django.contrib import admin
from .models import Bebe,AvanceDiario
# Register your models here.

@admin.register(Bebe)
class BebeCoordinadora(admin.ModelAdmin):
    list_display=('nombre','apellido_paterno','madre','sexo')
    
@admin.register(AvanceDiario)
class AvanceDiarioBebe(admin.ModelAdmin):
    list_display=('bebe','fecha')
    