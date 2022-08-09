from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    # configuración de nombre público de la app para que aparezca en el PA
    verbose_name = 'Gestor de servicios'
