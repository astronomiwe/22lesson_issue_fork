from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    discription = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='превью', null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за штуку')
    date_create = models.DateField(auto_now=True)
    date_last_change = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.product_discription}, {self.price}'

class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name='наименование')
    product_discription = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}, {self.product_discription}'

