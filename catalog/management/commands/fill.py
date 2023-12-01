from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'name': 'Сканер', 'product_discription': 'новый', 'category': 'техника', 'price':'1500', 'date_create': '2023-12-01'},
            {'name': 'Принтер', 'product_discription': 'бу', 'category': 'техника', 'price': '13500',
             'date_create': '2023-12-01'},
            {'name': 'Мышка', 'product_discription': 'новый', 'category': 'техника', 'price': '3000',
             'date_create': '2023-12-01'}

        ]

        products_for_create = []
        for product_item in products_list:
            products_for_create.append(
                Product(**product_item)
            )

            Product.objects.bulk_create(products_for_create)