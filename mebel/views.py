from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "main.html",)


def products(requset):
    return render(requset, "products.html")

