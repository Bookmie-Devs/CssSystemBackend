from django.contrib import admin
from .models import Product, ProductPayment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'type_of_product', 'price', 'created_at', 'last_updated')
    list_filter = ('type_of_product', 'created_at')
    search_fields = ('product_name', 'product_id')
    ordering = ('-created_at',)
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

class ProductPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'reference', 'transaction_validation_code', 'transaction', 'product', 'payed_at', 'payment_successful')
    list_filter = ('payment_successful', 'payed_at', 'transaction')
    search_fields = ('transaction_validation_code', 'payment_id', 'transaction')
    ordering = ('-payed_at',)
    list_per_page = 20

admin.site.register(ProductPayment, ProductPaymentAdmin)
