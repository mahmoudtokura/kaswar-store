from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .models import Category, Product, UserShippingDetail
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login
from .forms import SignupForm

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


def signupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)

            user_shipping_details = UserShippingDetail.objects.create(user=signup_user, shippingAddress=form.cleaned_data.get('shippingAddress'), shippingCity=form.cleaned_data.get('shippingCity'))
            user_shipping_details.save()

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('cart:cart_detail')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

