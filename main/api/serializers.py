from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from main.models import Post
from django.utils import timezone


class PostCreateSerializer(ModelSerializer):

    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_posted = serializers.HiddenField(default=timezone.now)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
            "date_posted",
        ]


class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "title",
            "author",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "date_posted",
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "date_posted",
            "visible",
            "semester",
        ]
