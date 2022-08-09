from django.contrib import admin
from .models import Category, Post

# Register your models here.
# * definiendo campos de lectura para el PA del modelo Category
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# * definiendo campos de lectura para el PA del modelo Post
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # * personalización del PA
    #                                               generado en la línea 25
    list_display = ('title', 'author', 'published', 'post_categories')
    # ordenando con dos elementos
    # ordering = ('author', 'published')
    # ordenando con un sólo elemento
    ordering = ('author',)
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published' # ayuda a generar una jerarquía de fechas en el PA
    list_filter = ('author__username', 'categories__name')

    # 'creando' un campo nuevo para que se muestre en el PA:
    def post_categories(self, obj):
        return ', '.join(c.name for c in obj.categories.all().order_by('name'))
    post_categories.short_description = 'Catogorías'



admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)