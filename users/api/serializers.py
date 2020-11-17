from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
    CharField,
    EmailField,
    ValidationError,
)

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db.models import Q

User = get_user_model()


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label="Email Address")
    email2 = EmailField(label="Confirm Email")
    password2 = CharField(write_only=True, label="Confirm Password")

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


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(label="Username", allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ["username", "password", "token"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        password = data["password"]
        username = data.get("username", None)
        if not username:
            raise ValidationError("A username is required to login.")

        user = User.objects.filter(  # CHECKS DATABASE TO SEE IF USER EXISTS
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username does not exist.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Credentials does not match.")

        data["token"] = "A TOKEN"
        return data


class UserDetailSerializer(
    ModelSerializer
):  # show details of user at main/api/serializers.py -> PostDetail
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
