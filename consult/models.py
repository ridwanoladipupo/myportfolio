from django.db import models

class Consult(models.Model):
    GRAPHICS = 'GR'
    MENTORSHIP = 'MR'
    SYSTEM_TROUBLESHOOTING ='ST'
    WEB_DEVELOPMENT = 'WD'
    CONSULT_LIST_CHOICES = (
        (GRAPHICS, 'Graphics Design'),
        (MENTORSHIP, 'Mentorship'),
        (SYSTEM_TROUBLESHOOTING, 'System Troubleshooting'),
        (WEB_DEVELOPMENT, 'Web Development'),
    )

    name = models.CharField(max_length = 100, null=True)
    email = models.EmailField(blank = False, null=True)
    categories = models.CharField(max_length = 2, choices= CONSULT_LIST_CHOICES, default= GRAPHICS)
    details = models.TextField(max_length = 1000, null=True)


    def __str__(self):
        name = self.name
        email = self.email
        categories = self.categories 
        details = self.details 

        return email