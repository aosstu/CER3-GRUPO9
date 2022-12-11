from django.shortcuts import render
from .models import Bebe
from .models import AvanceDiario

def vistaPadres(request):
    bebes = Bebe.objects.all()
    return render(request, 'Hospital/vistaProgenitores.html',{"bebes":bebes})

# Create your views here.
def login(request):
    return render(request,'Hospital/login.html')

def Avances(request):
    listAvances = AvanceDiario.objects.all()
    return render(request,'Hospital/verAvances.html',{"Avances":listAvances})