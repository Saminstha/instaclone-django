from django.urls import path
from .views import FeedView, CreatePostView, ProfileDetailView, ProfileUpdateView


urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='edit_profile'),
 

]
