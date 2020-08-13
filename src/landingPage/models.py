from django.db import models
from django.contrib import admin



class ContactFormEntry(models.Model):
    name= models.CharField(max_length=150, default="")
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=150, default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.subject
    

admin.site.register(ContactFormEntry)
