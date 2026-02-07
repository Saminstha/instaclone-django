from django.urls import path
from .views import FeedView, ProfileView, CreatePostView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('create/', CreatePostView.as_view(), name='create_post'),
]
