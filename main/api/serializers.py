from rest_framework.serializers import ModelSerializer

from main.models import Post


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
            "date_posted",
            "visible",
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
        ]
