from django.db import models

class Contact(models.Model):
    
    firstname = models.CharField(max_length = 100, null=True)
    lastname = models.CharField(max_length = 100, null=True)
    email = models.EmailField(blank = False)
    subject = models.TextField(max_length = 1000, null=True)


    def __str__(self):
        firstname = self.firstname
        lastname = self.lastname
        email = self.email
        subject = self.subject

        return email