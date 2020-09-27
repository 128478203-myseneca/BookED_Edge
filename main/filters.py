import django_filters

from .models import Post

class Filter_Feature(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = '__all__'