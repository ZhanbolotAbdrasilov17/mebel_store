from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/', category, name='category'),
    path('category/<int:category_id>/', CategoryDetail.as_view(), name='category'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('products/', products, name='products'),
    path('products/<int:products_id>/', ProductDetail.as_view(), name='products'),
]