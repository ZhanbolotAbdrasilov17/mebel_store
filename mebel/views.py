from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.utils.translation import activate, get_language

from django.conf import settings

from .forms import MailForm
from .models import *


def home(request):
    image_up_1 = DescriptionImage.objects.get(id=2)
    image_up_2 = DescriptionImage.objects.get(id=3)
    image_up_3 = DescriptionImage.objects.get(id=4)

    category_image_furniture_1 = ItemsFurniture.objects.get(id=1)
    category_image_furniture_2 = ItemsFurniture.objects.get(id=2)
    category_image_furniture_3 = ItemsFurniture.objects.get(id=3)
    category_image_furniture_4 = ItemsFurniture.objects.get(id=4)
    category_image_furniture_5 = ItemsFurniture.objects.get(id=5)
    category_image_furniture_6 = ItemsFurniture.objects.get(id=6)

    sales_products = Furniture.objects.filter(status='sale')

    news = News.objects.all()



    context = {"image_up_1": image_up_1, "image_up_2": image_up_2, "image_up_3": image_up_3,
               "cif1":category_image_furniture_1, "cif2":category_image_furniture_2, "cif3":category_image_furniture_3,
               "cif4":category_image_furniture_4, "cif5":category_image_furniture_5, "cif6":category_image_furniture_6,
               "sales_products": sales_products, news: "news"}
    return render(request, "main.html", context)


def products(request):
    categories = FurnitureCategory.objects.all()
    all_products = Furniture.objects.all()
    context = {"categories": categories, "all_products": all_products}
    return render(request, "products.html", context)


def shop(request):
    return render(request, "shop.html",)

def category(request):
    categories = FurnitureCategory.objects.all()
    last_10_products = Furniture.objects.all()
    context = {"categories": categories, "last_10_products": last_10_products}
    return render(request, "category.html", context)


class CategoryDetail(DetailView):
    model = FurnitureCategory
    template_name = "single_category.html"
    context_object_name = 'category'
    pk_url_kwarg = 'category_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = FurnitureCategory.objects.all()
        return context


class ProductDetail(DetailView):
    model = Furniture
    template_name = "single_product.html"
    context_object_name = 'products'
    pk_url_kwarg = 'products_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class SearchResultsView(ListView):
    model = Furniture
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")

        a = str(self.request).split()
        lang = a[-1].split('/')[1]
        # if lang == 'ky':
        #     print(1)
        #
        # if lang == 'ru':
        #     print(2)
        #
        # else:
        #     print(3)

        language = get_language()
        activate(language)

        object_list = Furniture.objects.filter(
            Q(title__icontains=query) | Q(category__title__icontains=query)
        )
        return object_list




class MailCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST)

        if form.is_valid():
            form.save()
            last_sender = Email.objects.last()
            message = f'Почта: {last_sender.address}\n'

            send_mail(
                'Почта клиента или партнера',
                message,
                'oriyental.treyd@mail.ru',
                ['orienttrade2016@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('home'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')

