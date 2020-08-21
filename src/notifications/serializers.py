from notifications.models import Notification
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('title', 'description', 'event_date', 'image_link', 'redirect_url', 'sound')
        