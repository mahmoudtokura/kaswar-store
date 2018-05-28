from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

admin.site.register(CartItem, CartItemAdmin)

