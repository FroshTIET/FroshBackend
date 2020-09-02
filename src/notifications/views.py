from django.shortcuts import render
from rest_framework import generics
from notifications.serializers import (
    FeaturedEventSerializer,
    NotificationSerializer,
    TimelineEventSerializer,
)
from notifications.models import FeaturedEvent, Notification, TimeLineEvent

# Create your views here.


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by("-event_date")
    serializer_class = NotificationSerializer


class FeaturedEventListView(generics.ListAPIView):
    queryset = FeaturedEvent.objects.all()
    serializer_class = FeaturedEventSerializer
    pagination_class = None


class TimelineEventListView(generics.ListAPIView):
    queryset = TimeLineEvent.objects.all().order_by("priority")
    serializer_class = TimelineEventSerializer
    pagination_class = None
