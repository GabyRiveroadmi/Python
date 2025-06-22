from django.shortcuts import render, get_object_or_404, redirect
from .models import Cartera, Billetera, Cinto
from .forms import CarteraForm, BilleteraForm, CintoForm

# --- CARTERAS ---
def lista_carteras(request):
    carteras = Cartera.objects.all()
    return render(request, 'myproyect/lista_carteras.html', {'carteras': carteras})

def detalle_cartera(request, pk):
    cartera = get_object_or_404(Cartera, pk=pk)
    return render(request, 'myproyect/detalle_cartera.html', {'cartera': cartera})

def crear_cartera(request):
    if request.method == 'POST':
        form = CarteraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carteras')
    else:
        form = CarteraForm()
    return render(request, 'myproyect/form_cartera.html', {'form': form})

def eliminar_cartera(request, pk):
    cartera = get_object_or_404(Cartera, pk=pk)
    if request.method == 'POST':
        cartera.delete()
        return redirect('lista_carteras')
    return render(request, 'myproyect/eliminar_cartera.html', {'cartera': cartera})

# --- BILLETERAS ---
def lista_billeteras(request):
    billeteras = Billetera.objects.all()
    return render(request, 'myproyect/lista_billeteras.html', {'billeteras': billeteras})

def detalle_billetera(request, pk):
    billetera = get_object_or_404(Billetera, pk=pk)
    return render(request, 'myproyect/detalle_billetera.html', {'billetera': billetera})

def crear_billetera(request):
    if request.method == 'POST':
        form = BilleteraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_billeteras')
    else:
        form = BilleteraForm()
    return render(request, 'myproyect/form_billetera.html', {'form': form})

def eliminar_billetera(request, pk):
    billetera = get_object_or_404(Billetera, pk=pk)
    if request.method == 'POST':
        billetera.delete()
        return redirect('lista_billeteras')
    return render(request, 'myproyect/eliminar_billetera.html', {'billetera': billetera})

# --- CINTOS ---
def lista_cintos(request):
    cintos = Cinto.objects.all()
    return render(request, 'myproyect/lista_cintos.html', {'cintos': cintos})

def detalle_cinto(request, pk):
    cinto = get_object_or_404(Cinto, pk=pk)
    return render(request, 'myproyect/detalle_cinto.html', {'cinto': cinto})

def crear_cinto(request):
    if request.method == 'POST':
        form = CintoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cintos')
    else:
        form = CintoForm()
    return render(request, 'myproyect/form_cinto.html', {'form': form})

def eliminar_cinto(request, pk):
    cinto = get_object_or_404(Cinto, pk=pk)
    if request.method == 'POST':
        cinto.delete()
        return redirect('lista_cintos')
    return render(request, 'myproyect/eliminar_cinto.html', {'cinto': cinto})


def home(request):
    return render(request, 'myproyect/base.html')

def about(request):
    return render(request, 'myproyect/about.html')



from django.contrib.auth.forms import UserCreationForm

# Vista registro de usuarios: 

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})
