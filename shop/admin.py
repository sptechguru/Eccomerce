from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders,OrderUpdate

# admin.site.register(Product)
# admin.site.register(Contact)
# admin.site.register(Orders)
# admin.site.register(OrderUpdate)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ['name', 'email', 'phone' ,'desc' ,'msg_id']
     ordering = ['name']
     search_fields = ('name', 'email' ,'phone' ,'msg_id')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
     list_display = ['order_id', 'amount', 'name' ,'email' ,'address' ,'city' ,'state','zip_code','phone']
     ordering = ['name']
     search_fields = ('name', 'email' ,'phone' ,'amount')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ['product_name', 'category' ,'subcategory' ,'price' ,'pub_date']
     ordering = ['product_name']
     search_fields = ('product_name', 'price' ,'category')


@admin.register(OrderUpdate)
class OrderUpdateAdmin(admin.ModelAdmin):
     list_display = ['update_id', 'order_id' ,'update_desc' ,'timestamp']
     ordering = ['order_id']
     search_fields = ('update_id', 'timestamp')
