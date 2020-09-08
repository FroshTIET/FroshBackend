from django.contrib.auth.models import User
from user_management.models import Student
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = (
            "id",
            "user",
            "rollNumber",
            "fullName",
            "branch",
            "gender",
            "birthday",
            "points",
            "phone_number",
            "whatsapp_link",
            "profile_pic",
        )


class ScoreBoardSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Student
        fields = ("user", "fullName", "points")
