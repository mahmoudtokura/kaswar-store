from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Category, Product

# Create your views here.
def index(request):
    return HttpResponse("Home page here")

def allProducts(request, category_slug=None):
    category_page = None
    products_list = None

    if category_slug: 
        category_page = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(category=category_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 6)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    return render(request, 'shop/allProducts.html', {'category':category_page,'products':products})


def productDetails(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception:
        pass
    return render(request, 'shop/product.html', {'product':product})

