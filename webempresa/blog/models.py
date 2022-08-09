from django.db import models
from django.db.models.deletion import CASCADE

# importando timezone para la fecha/hora de la creación del post
from django.utils.timezone import now

# importando a todos los usuarios registrados
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    #          hereda de user                         al eliminar un autor se borran todas sus entradas en cascada
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # relación entre category y post
    categories = models.ManyToManyField(Category, verbose_name='Categories', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title