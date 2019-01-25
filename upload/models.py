from django.db import models
from pyuploadcare.dj.models import ImageField

class Document(models.Model):
    description = models.CharField(max_length=200, null=True,)
    screenshot = ImageField()

    def __str__(self):
        description = self.description
        screenshot = self.screenshot

        return str(screenshot)
    

