from main.models import Post
from main.filters import PostFilter
from django.db.models import Q

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import PostLimitOffsetPagination, PageNumberPost
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .permissions import IsOwnerOrReadOnly

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostDeleteAPIView(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = PostDetailSerializer


class PostListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["title", "content", "author", "schools", "course", "classes"]
    pagination_class = PageNumberPost  # PageNumberPagination


"""    def get_queryset(self, *args, **kwargs):

        qs = Post.objects.filter(visible=True)
        query = self.request.GET.get("q")
        if query:
            qs = qs.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            ).distinct()
        return qs"""


class PostUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
