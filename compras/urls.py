from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path("", index, name="inicio"),
    path("agregar_auto/", views.agregar_auto, name="agregar_auto"),
    path("agregar_cliente/", views.agregar_cliente, name="agregar_cliente"),
    path("buscar/", views.buscar, name="buscar"),
    path("realizar_compra/", views.realizar_compra, name="realizar_compra"),
    path("buscar_cliente/", views.buscar_cliente, name="buscar_base"),
    path("update_cliente/<id_cliente>/", views.updateCliente, name="update_cliente"),
    path("delete_cliente/<id_cliente>/", views.deleteCliente, name="delete_cliente"),
]
