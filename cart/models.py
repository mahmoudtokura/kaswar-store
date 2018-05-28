from django.db import models
from shop.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    

    def __str__(self):
        return str(self.cart_id)

    def __unicode__(self):
        return str(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity * self.product.price
    

    def __str__(self):
        return self.product

    def __unicode__(self):
        return self.product


