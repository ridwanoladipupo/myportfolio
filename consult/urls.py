from django.urls import path
from . import views

app_name = 'consult'
urlpatterns = [
    path('', views.book, name="consult"),
]