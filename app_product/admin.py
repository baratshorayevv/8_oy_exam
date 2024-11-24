from django.contrib import admin
from .models import Category, Product, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'old_price', 'created')
    search_fields = ['title', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    search_fields = ['title']


class CartAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'user_id', 'quantity', 'created', 'update')
    search_fields = ['user_id', 'created']

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)

