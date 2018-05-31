from django.db import models

# Create your models here.
class Order(models.Model):
    transaction_id = models.CharField(max_length=250, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="NGN Order Total", blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True, verbose_name="Email Address")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shippingName = models.CharField(max_length=250, blank=True, null=True)
    shippingAddress = models.CharField(max_length=250, blank=True, null=True)
    shippingCity = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.transaction_id)

    def __unicode__(self):
        return str(self.transaction_id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="NGN Price")

    def sub_total(self):
        return self.price * self.quantity


    def __str__(self):
        return self.product

    def __unicode__(self):
        return self.product

