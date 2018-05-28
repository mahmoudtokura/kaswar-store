from .models import CartItem, Cart
from .views import _cart_id

def cart_counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart)
            for cart_item in cart_items:
                item_count += cart_item.quantity
        except Exception:
            item_count = 0
    return {'item_count':item_count}