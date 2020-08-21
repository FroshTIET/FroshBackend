from django.shortcuts import render
from rest_framework import generics
from notifications.serializers import NotificationSerializer
from notifications.models import Notification
# Create your views here.


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by('-event_date')
    serializer_class = NotificationSerializer
    