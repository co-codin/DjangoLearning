from django.urls import path
from .views import project_list, project_detail

app_name='budget'

urlpatterns = [
    path('', project_list, name='list'),
    path('<slug:project_slug>', project_detail, name='detail')
]