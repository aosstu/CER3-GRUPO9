from django.shortcuts import render
from .models import Bebe
from .models import AvanceDiario
from .forms import AvancesForm

def vistaPadres(request):
    bebes = Bebe.objects.all()
    return render(request, 'Hospital/vistaProgenitores.html',{"bebes":bebes})

# Create your views here.
def login(request):
    return render(request,'Hospital/login.html')

def Avances(request):
    listAvances = AvanceDiario.objects.all()
    return render(request,'Hospital/verAvances.html',{"Avances":listAvances})

def nuevoAvance(request):
    data = { "form": AvancesForm () }

    if request.method == 'POST':
        formulario = AvancesForm(data=request.POST, files= request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data['form'] = formulario

    return render(request,'Hospital/añadirAvance.html', data)