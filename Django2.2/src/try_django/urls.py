from django.contrib import admin
from django.urls import path, re_path, include

from blog.views import (
    blog_post_create_view,
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

    path('blog-new/', blog_post_create_view),
    path('blog/', include('blog.urls')),

    re_path(r'^pages?/$', about_page),
    re_path(r'^about/$', about_page),
    path('example/', example_page),
    path('contact/', contact_page),
]
