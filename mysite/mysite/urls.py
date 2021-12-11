from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Rest Framework
    path('', include('blog.urls')),  # Blog app
]
