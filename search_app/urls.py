from django.urls import path
from .views import searchResult

app_name = 'search_app'

urlpatterns = [
    path('', searchResult, name='searchResult')
]