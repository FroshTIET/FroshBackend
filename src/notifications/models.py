from django.db import models
import json
from django.conf import settings
import requests

# Create your models here.

TIMELINE_TYPE_CHOICES = [("checkpoint", "checkpoint"), ("line", "line")]


class Notification(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    image_link = models.CharField(max_length=500, default="")
    redirect_url = models.CharField(max_length=500, default="")
    sound = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sendNotification()

            super(Notification, self).save(*args, **kwargs)

    def sendNotification(self):
        url = "https://fcm.googleapis.com/fcm/send"
        payload = {
            "to": "/topics/allusers",
            "notification": {
                "title": self.title,
                "body": self.description,
                "mutable_content": True,
                "sound": "Tri-tone" if self.sound else "",
                "image": self.image_link,
            },
            "data": {"url": self.redirect_url,},
        }
        payload = json.dumps(payload)

        headers = {
            "Authorization": f"key={settings.FCM_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != 200:
            return None
        return response.json()["message_id"]


class FeaturedEvent(models.Model):
    title = models.CharField(max_length=255)
    image_link = models.TextField()
    redirect_url = models.TextField()

    def __str__(self):
        return self.title


class TourPicture(models.Model):
    title = models.CharField(max_length=255)
    image_link = models.TextField()

    def __str__(self):
        return self.title


class TimeLineEvent(models.Model):
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=255, blank=True, null=True)
    event_type = models.CharField(choices=TIMELINE_TYPE_CHOICES, max_length=255)
    duration = models.IntegerField(default=8)
    color = models.CharField(default="0xFF40C752", max_length=128)
    icon = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.title
