from django.shortcuts import render
from shop.models import Product, Category
from django.db.models import Q

# Create your views here.
def searchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        products = Product.objects.all().filter(Q(name__contains=query) | Q(decription__contains=query))
    return render(request, 'search_app/searchResult.html', {'query':query, 'products':products})
    
