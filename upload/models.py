from django.db import models

from pyuploadcare.dj.models import ImageField


class Document(models.Model):
    description = models.CharField(max_length=200, blank=False, null=False)
    screenshot = ImageField()

    def __str__(self):

        return self.screenshot
    

