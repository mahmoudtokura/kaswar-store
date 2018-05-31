from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_id','total','email','shippingName', 'shippingAddress', 'shippingCity','created','updated')

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','price', 'sub_total')

admin.site.register(OrderItem, OrderItemAdmin)
