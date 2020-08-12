from django.contrib import admin

from user_management.models import Student

admin.site.site_header = "Frosh Administration"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "rollNumber",
        "fullName",
        "points",
        "branch",
        "gender",
        "birthday",
        "phone_number",
    )
    list_filter = ("branch", "gender")

    search_fields = ["user__username", "fullName", "rollNumber", "phone_number"]
