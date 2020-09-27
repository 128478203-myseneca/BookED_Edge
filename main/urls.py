from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.home, name='Main-Home'),
    path('filter/', views.filters, name='Filter'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-Detail'), #set primarykey of posts which is the id
    path('post/<str:username>', UserPostListView.as_view(), name='User-Posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-Update'), #set primarykey of posts which is the id
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post-Delete'), #set primarykey of posts which is the id
    path('post/new/', PostCreateView.as_view(), name='Post-Create'), #set primarykey of posts which is the id
    path('market/', PostListView.as_view(), name='Main-Market'),
]
