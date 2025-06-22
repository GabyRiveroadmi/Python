from django.contrib import admin
from .models import Cartera, Billetera, Cinto

# Personalización para Cartera
class CarteraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color', 'precio')
    search_fields = ('nombre', 'color')

# Personalización para Billetera
class BilleteraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cuero', 'precio')
    search_fields = ('nombre', 'cuero')

# Personalización para Cinto
class CintoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'talle', 'precio')
    search_fields = ('nombre', 'talle')

# Registro de modelos en admin
admin.site.register(Cartera, CarteraAdmin)
admin.site.register(Billetera, BilleteraAdmin)
admin.site.register(Cinto, CintoAdmin)
