from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

]
