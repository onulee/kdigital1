from django.contrib import admin
from product.models import Product

@admin.register(Product)
class FboardAdmin(admin.ModelAdmin):
    list_display = ['p_no','p_name','p_unitPrice','p_fileName']
