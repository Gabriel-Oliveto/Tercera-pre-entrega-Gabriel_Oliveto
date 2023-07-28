from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .models import Auto, Cliente
from .forms import AutoForm, ClienteForm, BusquedaForm, CompraForm


# Create your views here.
def index(request):
    return render(request, "compras/index.html")


def agregar_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutoForm()
    return render(request, "compras/agregar_auto.html", {"form": form})


def agregar_cliente(request):
    ctx = {"clientes": Cliente.objects.all()}
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "compras/buscar_base.html", ctx)
    else:
        form = ClienteForm()
    return render(request, "compras/agregar_cliente.html", {"form": form})


def realizar_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "inicio"
            )  # Redireccionar a la página principal o donde desees
    else:
        form = CompraForm()
    return render(request, "compras/realizar_compra.html", {"form": form})


def buscar(request):
    if request.method == "POST":
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data["busqueda"]
            resultados = Auto.objects.filter(marca__icontains=busqueda)
    else:
        form = BusquedaForm()
        resultados = Auto.objects.all()
    return render(
        request, "compras/buscar.html", {"form": form, "resultados": resultados}
    )


def buscar_cliente(request):
    ctx = {"clientes": Cliente.objects.all()}
    if request.method == "POST":
        query = request.POST.get("query")
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=query)
            | Q(apellido__icontains=query)
            | Q(direccion__icontains=query)
        )
        return render(
            request,
            "compras/buscar_base.html",
            {
                "clientes": clientes,
            },
        )
    return render(request, "compras/buscar_base.html", ctx)


def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data.get("nombre")
            cliente.apellido = form.cleaned_data.get("apellido")
            cliente.direccion = form.cleaned_data.get("direccion")
            cliente.save()
            return redirect(reverse_lazy("buscar_base"))
    else:
        form = ClienteForm(
            initial={
                "nombre": cliente.nombre,
                "apellido": cliente.apellido,
                "direccion": cliente.direccion,
            }
        )
    return render(request, "compras/updateForm.html", {"form": form})


def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy("buscar_base"))
