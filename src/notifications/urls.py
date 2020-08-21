from django.urls import path
from notifications.views import NotificationListView


urlpatterns = [
    path('all/', NotificationListView.as_view(), name='notification-list'),
]
