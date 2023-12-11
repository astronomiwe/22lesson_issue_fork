from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'SkyStore - Главная'
    }
    return render(request, 'catalog/index.html', context=context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'catalog/contact.html', context)


def product(request, pk):
    get_product = get_object_or_404(Product, id=pk)
    context = {
        'object': get_product,
        'title': 'Продукт'
    }
    return render(request, 'catalog/product.html', context=context)
