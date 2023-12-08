from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, categories, category_products, contact

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', index, name='categories'),
    path('<int:pk>/products/', category_products, name='category_products'),
    path('contact/', contact),

]