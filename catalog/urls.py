from django.urls import path

from catalog.views import home, contacts


urlpatterns = [
    path('', home, name='index'),
    path('contacts/', contacts, name='contacts'),
]