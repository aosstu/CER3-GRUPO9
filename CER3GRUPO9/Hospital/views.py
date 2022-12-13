from django.shortcuts import render, redirect, get_object_or_404
from .models import Bebe
from .models import AvanceDiario
from .forms import AvancesForm

def vistaPadres(request):
    bebes = Bebe.objects.all()
    return render(request, 'Hospital/vistaProgenitores.html',{"bebes":bebes})

# Create your views here.
def login(request):
    return render(request,'Hospital/index.html')

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

def modificarAvance(request,id):
    avanceDiario = get_object_or_404(AvanceDiario, id=id)
    data= {
        'form': AvancesForm(instance=avanceDiario)
    }
    if request.method == 'POST':
        formulario = AvancesForm(data=request.POST, instance=avanceDiario, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Modificado Correctamente"
            redirect(to='verAvances')
        else:
            data['form'] = formulario

    return render(request, 'Hospital/modificarAvance.html',data)

def eliminarAvance(request,id):
    avanceDiario = get_object_or_404(AvanceDiario, id=id)
    avanceDiario.delete()
    redirect(to="verAvances")