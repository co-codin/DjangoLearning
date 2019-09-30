from django.http import JsonResponse

from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()
    data = {
        "products": list(products.values())
    }
    response = JsonResponse(data)
    return response
