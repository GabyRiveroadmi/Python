from django.shortcuts import render
from .forms import CarteraForm, BilleteraForm, CintoForm, BuscarForm
from .models import Cartera

def index(request):
    return render(request, 'index.html')

def agregar_cartera(request):
    form = CarteraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agregar_cartera.html', {'form': form})

def agregar_billetera(request):
    form = BilleteraForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agregar_billetera.html', {'form': form})

def agregar_cinto(request):
    form = CintoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'agregar_cinto.html', {'form': form})

def buscar_producto(request):
    form = BuscarForm()
    return render(request, 'buscar_producto.html', {'form': form})

def resultados_busqueda(request):
    nombre = request.GET.get('nombre', '')
    resultados = Cartera.objects.filter(nombre__icontains=nombre)
    return render(request, 'resultados_busqueda.html', {'resultados': resultados})
