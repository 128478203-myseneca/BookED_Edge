from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from rest_framework import serializers
from rest_framework.serializers import ValidationError
from main.models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = serializers.EmailField(label="Email Address")
    email2 = serializers.EmailField(label="Confirm Email")
    password2 = serializers.CharField(write_only=True, label="Confirm Password")

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "email2",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        user_obj = User(
            first_name=first_name, last_name=last_name, username=username, email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails does not match")

        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This email address has been taken by another user.")
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get("password")
        password2 = value
        if password1 != password2:
            raise ValidationError("Passwords does not match")
        return value
