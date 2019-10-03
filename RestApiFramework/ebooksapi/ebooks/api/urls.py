from django.urls import path
from ebooks.api.views import (
    EbookListCreateAPIView, EbookDetailAPIView
)

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="ebook-list"),
    path("ebooks/<int:pk>", EbookDetailAPIView.as_view(), name="ebook-detail")
]