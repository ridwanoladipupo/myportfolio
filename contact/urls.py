from django.urls import path

from .views import contactme


app_name = "contact"

urlpatterns = [
    path('', contactme, name="contact"),
]