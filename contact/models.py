from django.db import models


class Contact(models.Model):    
    firstname = models.CharField(max_length=100, null=False)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.TextField(max_length=1000, null=False)

    def __str__(self):
        return self.email