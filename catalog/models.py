from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    discription = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена за штуку')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.product_discription}, {self.price}'

class Category(models.Model):
    product = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, verbose_name='наименование')
    product_discription = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.product_discription}'

