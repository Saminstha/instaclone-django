from django.urls import path
from .views import FeedView, CreatePostView, ProfileDetailView, ProfileUpdateView, UserProfileView, FollowToggleView


urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('u/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('u/<str:username>/follow/', FollowToggleView.as_view(), name='follow_toggle'),


]
