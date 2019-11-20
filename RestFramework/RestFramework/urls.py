from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', include('cars.urls')),
    path('api/v1/base-auth/', include('rest_framework.urls'))
]
