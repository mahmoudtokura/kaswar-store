from django.urls import path
from .views import add_to_cart, cart_detail, cart_remove_item, delete_cart_item

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>', cart_remove_item, name='cart_remove_item'),
    path('delete/<int:product_id>', delete_cart_item, name='delete_cart_item')
]
