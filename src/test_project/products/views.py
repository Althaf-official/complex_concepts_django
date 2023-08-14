from django.shortcuts import render

from .models import Product

def product_detail_view():
    obj = Product.objects.get(id=1)
    return render(request, "product/detail.html", {})