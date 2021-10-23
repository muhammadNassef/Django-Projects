from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('CarRental/', include('CarRental.urls')),
]
