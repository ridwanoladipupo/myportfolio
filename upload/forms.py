from django import forms

from .models import Document
from pyuploadcare.dj.models import ImageField


class DocumentForm(forms.ModelForm):
    screenshot = ImageField()
    class Meta:
        model = Document
        fields = ['description','screenshot',]