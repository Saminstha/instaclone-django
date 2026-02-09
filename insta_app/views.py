from django.views.generic import ListView, CreateView, TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Post, Follow, Profile
from .forms import UserUpdateForm, ProfileUpdateForm


#  FEED VIEW
class FeedView(ListView):
    model = Post
    template_name = 'insta_app/feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


#  CREATE POST
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'caption']
    template_name = 'insta_app/create_post.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#  PROFILE (Logged-in User)
class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'insta_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['profile_user'] = user
        context['posts'] = Post.objects.filter(user=user)
        context['posts_count'] = Post.objects.filter(user=user).count()
        context['followers_count'] = Follow.objects.filter(following=user).count()
        context['following_count'] = Follow.objects.filter(follower=user).count()

        return context


#  EDIT PROFILE
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'insta_app/edit_profile.html'

    def get(self, request, *args, **kwargs):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        return self.render_to_response({
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')

        return self.render_to_response({
            'user_form': user_form,
            'profile_form': profile_form
        })


class UserProfileView(DetailView):
    model = Profile
    template_name = 'insta_app/user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(Profile, user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        context['posts'] = Post.objects.filter(user=profile.user)
        context['posts_count'] = context['posts'].count()
        context['followers_count'] = profile.followers.count()
        context['following_count'] = profile.following.count()

        return context