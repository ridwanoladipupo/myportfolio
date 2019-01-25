from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', include('contact.urls')),
    path('consult/', include('consult.urls')),
]