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
    return render(request, "main.html",)


def products(requset):
    categories = FurnitureCategory.objects.all()
    all_products = Furniture.objects.all()
    context = {"categories": categories, "all_products": all_products}
    return render(requset, "products.html", context)


def category(requset):
    categories = FurnitureCategory.objects.all()
    last_10_products = Furniture.objects.all()
    context = {"categories": categories, "last_10_products": last_10_products}
    return render(requset, "category.html", context)


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
        context['text'] = FurnitureFullDescription.objects.all()
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
                ['itpythonzhanbolot@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Письмо отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('home'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')

