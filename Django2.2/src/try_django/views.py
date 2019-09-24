from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
    return render(request, "home.html", {})

def about_page(request):
    return render(request, "about.html", {"title": "About"})

def contact_page(request):
    return HttpResponse('<h1>contact</h1>')

def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)