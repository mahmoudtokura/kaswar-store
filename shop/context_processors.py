from .models import Category

def category_menu(request):
    category_links = Category.objects.all()
    return {'category_links':category_links}