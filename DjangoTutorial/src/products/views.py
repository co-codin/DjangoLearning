from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
    object = Product.objects.get(id=1)

    context = {
        'object': object
    }

    return render(request, "products/product_detail.html", context)
