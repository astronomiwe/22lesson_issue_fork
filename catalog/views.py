from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'SkyStore - Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'SkyStore - Все наши товары'
    }
    return render(request, 'products/categories.html', context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.object.filter(category_id=pk),
        'title': f'SkyStore - Все наши товары {category_item.name}'
    }
    return render(request, 'products/products.html', context)