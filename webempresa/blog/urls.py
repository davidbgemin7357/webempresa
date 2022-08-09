from django.urls import path
from .views import blog, category

urlpatterns = [
    path('', blog, name='blog'),
    path('category/<int:category_id>/', category, name='category')
]