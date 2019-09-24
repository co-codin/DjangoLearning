from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = { 'object_list': qs }
    return render(request, template_name, context)

def blog_post_create_view(request):
    # create objects
    # ? use a form
    # request.user -> return something
    template_name = 'blog_post_create.html'
    context = { 'form': None }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = { 'object': obj }
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {'object': obj}
    return render(request, template_name, context)