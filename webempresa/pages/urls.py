from django.urls import path
from .views import page

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', page, name='page')
]