from django.urls import path
from .views import project_list

app_name='budget'

urlpatterns = [
    path('', project_list, name='list')
]