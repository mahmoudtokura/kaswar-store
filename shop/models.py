from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    decription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'cartegories'


    def get_absolute_url(self):
        return reverse('shop:products_by_category', kwargs={'category_slug': self.slug})


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    decription = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'


    def get_absolute_url(self):
        return reverse('shop:productDetails', kwargs={'category_slug': self.category.slug,'product_slug': self.slug})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class UserShippingDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shippingAddress = models.CharField(max_length=250, blank=True, null=True)
    shippingCity = models.CharField(max_length=250, blank=True, null=True)


    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
