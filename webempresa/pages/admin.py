from django.contrib import admin
from .models import Page

# Register your models here.
# * configuración de campos que son solo de lectura
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # orden de los campos:
    list_display = ('title', 'order')


# * registrando la app para el PA
admin.site.register(Page, PageAdmin)