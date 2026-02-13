from django.urls import path
from .views import AddCommentView, FeedView, CreatePostView, LikeToggleView, PostDetailView, ProfileDetailView, ProfileUpdateView, UserProfileView, FollowToggleView


urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('u/<str:username>/', UserProfileView.as_view(), name='user_profile'),
    path('u/<str:username>/follow/', FollowToggleView.as_view(), name='follow_toggle'),
    path('post/<int:post_id>/like/', LikeToggleView.as_view(), name='like_toggle'),
    path('comment/<int:post_id>/', AddCommentView.as_view(), name='add_comment'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),



]
