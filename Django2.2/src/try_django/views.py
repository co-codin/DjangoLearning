from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, "home.html", {})

def about_page(request):
    return HttpResponse('<h1>about</h1>')

def contact_page(request):
    return HttpResponse('<h1>contact</h1>')

def example_page(request):
    return HttpResponse('<h1>example</h1>')
