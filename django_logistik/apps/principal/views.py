from django.shortcuts import render, redirect
from .models import Transportista
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    column_names = [field.name for field in Conductor._meta.get_fields()][2:10]
    conductores = Conductor.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': conductores,
    }

    return render(request, 'principal/listas/listar_conductores.html', data)
    # return render(request, 'principal/home.html')

def login(request):
    return render(request, 'principal/registration/login.html')

@login_required
def crear_transportista(request):
    data = { 'form': TransportistaForm() }

    if request.method == 'POST':
        formulario = TransportistaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Transportista creado."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_transportista.html', data)

@login_required
def crear_camion(request):
    data = { 'form': CamionForm() }

    if request.method == 'POST':
        formulario = CamionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Camión creado."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_camion.html', data)

@login_required
def crear_conductor(request):
    data = { 'form': ConductorForm() }

    if request.method == 'POST':
        formulario = ConductorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Conductor creado."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_conductor.html', data)

@login_required
def crear_cliente(request):
    data = { 'form': ClienteForm() }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cliente creado."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_cliente.html', data)

@login_required
def crear_albaran(request):
    data = { 'form': AlbaranForm() }

    if request.method == 'POST':
        formulario = AlbaranForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Albaran creado."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_albaran.html', data)

@login_required
def crear_mercancia(request):
    data = { 'form': MercanciaForm() }

    if request.method == 'POST':
        formulario = MercanciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mercancia creada."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_mercancia.html', data)

@login_required
def modificar_mercancia(request, id):
    mercancia = Mercancia.objects.get(id = id)

    if request.method == 'GET':
        form = MercanciaForm(instance = mercancia)
        contexto = {
            'form': form
        }
    elif request.method == 'POST':
        form = MercanciaForm(request.POST, instance = mercancia)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'modificar_mercancia.html', contexto)

@login_required
def modal_modificar_mercancia(request):
    mercancias = Mercancia.objects.all()
    return render(request, 'principal/modal_modificar_mercancia.html', {"mercancias": mercancias})


@login_required
def crear_ruta(request):
    data = { 'form': RutaForm() }

    if request.method == 'POST':
        formulario = RutaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Ruta creada."
        else:
            data["form"] = formulario

    return render(request, 'principal/crear/crear_ruta.html', data)

@login_required
def listar_transportistas(request):
    column_names = [field.name for field in Transportista._meta.get_fields()][3:9]
    transportistas = Transportista.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': transportistas,
    }

    return render(request, 'principal/listas/listar_transportistas.html', data)

@login_required
def listar_conductores(request):
    column_names = [field.name for field in Conductor._meta.get_fields()][2:10]
    conductores = Conductor.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': conductores,
    }

    return render(request, 'principal/listas/listar_conductores.html', data)

@login_required
def listar_camiones(request):
    column_names = [field.name for field in Camion._meta.get_fields()][3:17]
    camiones = Camion.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': camiones,
    }

    return render(request, 'principal/listas/listar_camiones.html', data)

@login_required
def listar_clientes(request):
    column_names = [field.name for field in Cliente._meta.get_fields()][2:14]
    clientes = Cliente.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': clientes,
    }

    return render(request, 'principal/listas/listar_clientes.html', data)

@login_required
def listar_albaranes(request):
    column_names = [field.name for field in Albaran._meta.get_fields()][2:8]
    albaranes = Albaran.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': albaranes,
    }

    return render(request, 'principal/listas/listar_albaranes.html', data)

@login_required
def listar_mercancias(request):
    column_names = [field.name for field in Mercancia._meta.get_fields()]
    mercancias = Mercancia.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': mercancias,
    }

    return render(request, 'principal/listas/listar_mercancias.html', data)

@login_required
def listar_rutas(request):
    column_names = [field.name for field in Ruta._meta.get_fields()][1:6]
    rutas = Ruta.objects.all()
    
    data = {
        'column_names': column_names,
        'row_values': rutas,
    }

    return render(request, 'principal/listas/listar_rutas.html', data)