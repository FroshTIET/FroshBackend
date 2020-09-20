from django.contrib import admin
from froshwall.models import Tweet
# Register your models here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = [
        "content",
        "username",
        "timestamp",
        "approved"
    ]

    list_filter = [
        "approved",
    ]

    list_editable = [
        "approved",

    ]


