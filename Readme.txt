Autor : Gabriel Oliveto

Objetivo del TP Presentado

Objetivos generales

Desarrollar una WEB Django con patrón MVT subida a Github.
Se debe entregar

Link de GitHub con el proyecto totalmente subido a la plataforma.
Proyecto Web Django con patrón MVT que incluya:
Herencia de HTML.
Por lo menos 3 clases en models.
Un formulario para insertar datos a todas las clases de tu models.
Un formulario para buscar algo en la BD
Readme que indique el orden en el que se prueban las cosas y/o donde están las funcionalidades.

1. Desarrollo de las siguientes clases
   -class Auto
   Atributos: Marca, Modelo y precio
   -class Cliente
   Atributos: Nombre, Apellido y Direccion
   -class Compra
   Atributos: Auto, Cliente y Fecha

2. Funciones utilizadas
   -def agregar_auto
   -def agregar_cliente
   -def realizar_compra
   -def buscar
   -def buscar_cliente
   -def updateCliente
   -def deleteCliente

3. Ejemplo de uso
   1.Abrir la carpeta donde se encuentra el proyecto y desde ahi abrir la consola de comandos(CMD).
   2.Levantar el servidor usando el comando python manage.py runserver
   3.Entrar desde algun navegador de internet a la direccion IP que nos provee el runserver(por defaul 127.0.0.1:8000) y despues de la direccion IP agragar /compras
   4.Dentro de la pagina ya se encuentran cargados datos, pero si se quiere usar con datos nuevos, primero hay que agregar un Auto, luego agregar un cliente para despues poder realizar la compra.
   5.Desde el listado de Autos se pueden visualizar todos los autos cargados en la base de datos, en caso de que sea muy larga la lista se puede buscar por marca de auto y nos devuelve todos los modelos cargados en la base de datos por Marca.
   6.Desde Clientes se puede ver todo el listado de cliente, igual que en el listado de autos que la lista sea muy larga se puede realizar una busqueda por Nombre, Apellido o direccion. Desde la misma pagina se puede agregar "con el signo +",  modificar o borrar clientes.
   7.Desde la Opcion administracion se puede manejar toda la base de datos, el "usuario" es admin y la "password" es admin123456.
