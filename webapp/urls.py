
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('rsapp.urls')),
    path('', include('listings.urls')),
    path('', include('realtors.urls')),
    path('admin/', admin.site.urls),
]
