from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view

urlpatterns = [
    path('', home_view, name="home"),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),
    path('admin/', admin.site.urls)
]
