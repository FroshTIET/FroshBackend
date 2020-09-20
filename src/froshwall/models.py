from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    approved = models.BooleanField(default=None, null=True, blank=True)

    timestamp = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return str(self.content)

