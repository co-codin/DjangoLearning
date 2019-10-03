from django.contrib import admin
from ebooks.models import Review, Ebook

# Register your models here.
admin.site.register(Ebook)
admin.site.register(Review)