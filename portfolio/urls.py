from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('upload.urls')),
    path('', include('consultation.urls')),
]
