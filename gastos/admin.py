from django.contrib import admin

from .models import Gastos
# Register your models here.
class GastosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'gasto_fecha', 'proveedor', 'numero_factura', 'costo_total')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 25

admin.site.register(Gastos, GastosAdmin)
