from django.forms import ModelForm
from .models import Consult

class ConsultForm(ModelForm):
    class Meta:
        model = Consult
        fields = ['name','email', 'categories', 'details']