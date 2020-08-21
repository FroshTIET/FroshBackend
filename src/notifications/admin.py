from django.contrib import admin
from notifications.models import Notification
from django.contrib import messages
# Register your models here.

class IncorrectTokenException(Exception):
    def __str__(self):
        return "The authentication token was incorrect"
    pass

def resend_notification(modeladmin, request, queryset):
    try:
        for notifi in queryset:
            if  not notifi.sendNotification():
                raise IncorrectTokenException
            
        modeladmin.message_user(request, "All notifications were sent successfully.", level=messages.INFO, extra_tags='', fail_silently=False)
    except Exception as ಠ_ಠ:
        modeladmin.message_user(request, f"Sending notifications failed. Error: {ಠ_ಠ}", level=messages.ERROR, extra_tags='', fail_silently=False)

resend_notification.short_description = "Resend Selected Notifications"


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "description",
        "event_date",
        "sound"
    )

    search_fields = ["title", "description", "event_date", "redirect_url"]
    actions = [resend_notification,]
    