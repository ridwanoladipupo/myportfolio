from django.urls import path
from .views import CreateViewWork,UploadView

app_name = 'upload'
urlpatterns = [
    path('', CreateViewWork, name="view"),
    path('upload/', UploadView, name="upload"),
]
