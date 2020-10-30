from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='Main-Home'),
    path('filter/', views.filters, name='Filter'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-Detail'), #set primarykey of posts which is the id
    path('post/<str:username>', UserPostListView.as_view(), name='User-Posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-Update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post-Delete'), 
    path('post/new/', PostCreateView.as_view(), name='Post-Create'), 
    path('market/', PostListView.as_view(), name='Main-Market'),
   
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
