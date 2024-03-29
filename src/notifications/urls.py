from django.urls import path
from notifications.views import (
    FeaturedEventListView,
    NotificationListView,
    TimelineEventListView, TourEventListView,
)


urlpatterns = [
    path("notifications/", NotificationListView.as_view(), name="notification-list"),
    path("featured/", FeaturedEventListView.as_view(), name="featured-event-list"),
    path("timeline/", TimelineEventListView.as_view(), name="timeline-event-list"),
    path("virtualtour/", TourEventListView.as_view(), name='tour'),
]
