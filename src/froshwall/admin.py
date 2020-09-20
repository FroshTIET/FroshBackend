from django.contrib import admin
from froshwall.models import Tweet
# Register your models here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    def name(self, object):
        return object.user.first_name

    list_display = [
        "content",
        "name",
        "timestamp",
        "approved"
    ]

    list_filter = [
        "approved",
    ]

    list_editable = [
        "approved",

    ]


