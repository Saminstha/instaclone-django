from django.urls import path
from .views import RegisterView, CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Custom login view to show error messages
    path('login/', CustomLoginView.as_view(), name='login'),

    # Logout view (redirects to login page after logout)
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # Registration view
    path('register/', RegisterView.as_view(), name='register'),
]