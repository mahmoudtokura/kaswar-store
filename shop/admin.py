from django.contrib import admin
from .models import Category, Product, UserShippingDetail

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','available','created','updated')
    list_editable =('price','stock','available')
    prepopulated_fields={'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

class UserShippingDetailAdmin(admin.ModelAdmin):
    list_display = ('user','shippingAddress','shippingCity')
    list_editable =('shippingAddress','shippingCity')

admin.site.register(UserShippingDetail, UserShippingDetailAdmin)

