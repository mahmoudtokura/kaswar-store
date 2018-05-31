from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, UserShippingDetail
from .models import Cart, CartItem
from order.models import Order, OrderItem
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity <= cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter =+ cart_item.quantity
    except Exception:
        pass
    
    paystack_data_key = settings.PAYSTACK_PUBLISHABLE_KEY
    transaction_id = uuid.uuid4()
    paystack_total = total * 100

    #Creating the order
    user = User.objects.get(username=request.user.username)
    print('User is: ',user)
    customer_datails = UserShippingDetail.objects.get(user=user)
    if request.method == 'POST':
        order = Order.objects.create(transaction_id=transaction_id, total=total, email=request.user.email, shippingName=request.user.first_name+' '+request.user.last_name, shippingAddress=customer_datails.shippingAddress, shippingCity=customer_datails.shippingCity)
        order.save()
        for item in cart_items:
            order_item = OrderItem.objects.create(order=order, product=item.product.name, quantity=item.quantity, price=item.product.price)
            order_item.save()

            product = Product.objects.get(id=item.product.id)
            product.stock = int(item.product.stock - item.quantity)
            product.save()
            item.delete()
        return redirect('shop:allProducts')
        
    return render(request, 'cart/cart_detail.html', {'cart_items':cart_items, 'total':total, 'counter':counter, 'paystack_data_key':paystack_data_key, 'transaction_id':transaction_id, 'paystack_total':paystack_total})


def cart_remove_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')


def delete_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart:cart_detail')