from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from rest_framework import serializers
from main.models import Post
from django.utils import timezone
from users.api.serializers import UserDetailSerializer


class PostCreateSerializer(ModelSerializer):

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

        # extra_kwargs = {"title": {"required": False}, "content": {"required": False}} #takes away the required parameter from fields

    def get_validation_exclusions(self):
        exclusions = super(PostUpdateSerializer, self).get_validation_exclusions()
        return exclusions + ["title", "content"]


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
    url = serializers.HyperlinkedIdentityField(
        view_name="Detail-API", lookup_field="pk"
    )
    author = SerializerMethodField()
    schools = SerializerMethodField()
    course = SerializerMethodField()
    classes = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "url",
            "title",
            "author",
            "schools",
            "course",
            "classes",
            "date_posted",
        ]

    def get_author(
        self, obj
    ):  # this function is used to return the actual name of the object not the number id
        return str(obj.author.username)

    def get_schools(self, obj):
        return str(obj.schools)

    def get_course(self, obj):
        return str(obj.course)

    def get_classes(self, obj):
        return str(obj.classes)


class PostDetailSerializer(ModelSerializer):
    author = UserDetailSerializer(read_only=True)
    schools = SerializerMethodField()
    course = SerializerMethodField()
    classes = SerializerMethodField()
    post_img = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "content",
            "schools",
            "course",
            "classes",
            "isbn",
            "semester",
            "visible",
            "sponsored",
            "date_posted",
            "post_img",
        ]

    def get_schools(self, obj):
        return str(obj.schools)

    def get_course(self, obj):
        return str(obj.course)

    def get_classes(self, obj):
        return str(obj.classes)

    def get_post_img(self, obj):
        try:
            post_img = obj.post_img.url
        except:
            post_img = None
        return str("http://127.0.0.1:8000" + post_img)  # CHANGE THIS
