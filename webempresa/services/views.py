from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    # queryset para ver todos los servicios:
    services = Service.objects.all()
                                                # diccionario que será importado en el template services.html
    return render(request, "services/services.html", {'services':services})