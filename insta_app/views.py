from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Post

class FeedView(ListView):
    model = Post
    template_name = 'insta_app/feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class ProfileView(ListView):
    model = Post
    template_name = 'insta_app/profile.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.profile_user = get_object_or_404(
            User, username=self.kwargs['username']
        )
        return Post.objects.filter(user=self.profile_user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.profile_user
        return context

class CreatePostView(CreateView):
    model = Post
    fields = ['image', 'caption']
    template_name = 'insta_app/create_post.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
