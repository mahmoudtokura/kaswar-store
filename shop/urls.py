from django.urls import path
from .views import allProducts, productDetails


app_name='shop'

urlpatterns = [
    path('', allProducts, name="allProducts"),
    path('<slug:category_slug>/', allProducts, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', productDetails, name='productDetails')
]