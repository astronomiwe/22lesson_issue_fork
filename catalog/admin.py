from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'product_discription')

#Через инструмент shell заполните список категорий, а
# также выберите список категорий, применив произвольные
# рассмотренные фильтры. В качестве решения приложите скриншот.