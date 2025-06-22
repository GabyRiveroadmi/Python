from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myproyect.urls')),  # inicio y app principal
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password
]
