from django.contrib import admin
from .models import Categoria, Planta, detalle_boleta, Boleta
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Planta)
admin.site.register(detalle_boleta)
admin.site.register(Boleta)