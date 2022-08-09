from django.contrib import admin
from .models import Service

# Register your models here.
# configuración de campos que son solo de lectura
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# registrando la app para el PA
admin.site.register(Service, ServiceAdmin)