from django.contrib import admin
from django.urls import path, re_path

from blog.views import (
    blog_post_create_view,
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view
)

from .views import (
    home_page,
    about_page,
    contact_page,
    example_page
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),

    path('blog/', blog_post_list_view),

    path('blog/<str:slug>/', blog_post_detail_view),
    path('blog/<str:slug>/edit/', blog_post_edit_view),
    path('blog/<str:slug>/delete/', blog_post_delete_view),

    path('blog-new/', blog_post_create_view),

    re_path(r'^pages?/$', about_page),
    re_path(r'^about/$', about_page),
    path('example/', example_page),
    path('contact/', contact_page),
]
