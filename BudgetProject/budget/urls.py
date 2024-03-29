from django.urls import path
from .views import project_list, project_detail, ProjectCreateView

urlpatterns = [
    path('', project_list, name='list'),
    path('add', ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', project_detail, name='detail')
]