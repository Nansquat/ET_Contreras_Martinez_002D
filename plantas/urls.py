from django.urls import path
from plantas.views import *
#CON LAS COMILLAS SIMPLES EN path('',) EL SERVIDOR
#SE ABRE EN EL HTML DE INDEX
urlpatterns = [
    path('',index, name="index"),
    path('nosotros/',nosotros, name="nosotros"),
    path('galeria/',galeria, name="galeria"),
    path('plantas/',plantas, name="plantas"),
    path('crear/',crear, name="crear"),
    path('eliminar/<id>',eliminar, name="eliminar"),
    path('modificar/<id>',modificar, name="modificar"),
    path('contacto/',contacto, name="contacto"),
    path('registrar/', registrar, name="registrar"),

    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]