from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
)
from django.conf import settings

urlpatterns = [
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)