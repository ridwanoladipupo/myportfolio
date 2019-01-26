from django.urls import path

from .views import book


app_name = 'consult'

urlpatterns = [
    path('', book, name="consult"),
]