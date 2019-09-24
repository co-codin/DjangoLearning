from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import BlogPost

from .forms import BlogPostForm

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
    form = BlogPostForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        title = form.cleaned_data['title']
        # obj = BlogPost.objects.create(title=title)
        BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template_name = 'form.html'
    context = { 'form': form }
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
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