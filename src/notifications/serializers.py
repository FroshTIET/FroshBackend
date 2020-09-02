from notifications.models import Notification, FeaturedEvent, TimeLineEvent
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('title', 'description', 'event_date', 'image_link', 'redirect_url', 'sound')
    
class FeaturedEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedEvent
        fields = ('title', 'image_link', 'redirect_url')
    

class TimelineEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLineEvent
        fields = ('title', 'date', 'event_type', 'duration', 'color', 'icon')
         