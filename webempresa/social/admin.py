from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    # * configurando los campos de solo lectura
    readonly_fields = ('created', 'updated')
    # * configuración para que no se pueda modificar la clave del link
    def get_readonly_fields(self, request, obj=None):
        # si en tiempo de ejecución detectamos que el usuario que está accediento al PA forma parte del grupo personal, read_only_fields tendrá el valor de la siguiente tupla:
        if request.user.groups.filter(name='Personal').exists():
            # return ('created', 'updated', 'key', 'name')
            return ('key', 'name')
        else:
            return ('created', 'updated')



admin.site.register(Link, LinkAdmin)