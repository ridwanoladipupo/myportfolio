from django.urls import include, path

from .views import index


urlpatterns = [
    path('', index, name="index"),
    path('contact/', include('contact.urls')),
    path('consult/', include('consult.urls')),
]