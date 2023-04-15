from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView
from django.conf import settings


from .models import *

def home(request):
    return render(request, "main.html",)


def products(requset):
    product = Furniture.objects.all()
    context = {"product": product}
    return render(requset, "products.html", context)

class ProductDetail(DetailView):
    model = Furniture
    template_name = "single_product.html"
    context_object_name = 'products'
    pk_url_kwarg = 'products_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['text'] = FurnitureFullDescription.objects.all()
        return context