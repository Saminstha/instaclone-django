from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Post, Follow, Profile, Comment
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages



#  FEED VIEW
class FeedView(ListView):
    model = Post
    template_name = 'post/feed.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


#  CREATE POST
class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'caption']
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#  PROFILE (Logged-in User)

class ProfileDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile

        context['profile'] = profile
        context['posts'] = Post.objects.filter(user=self.request.user)
        context['posts_count'] = context['posts'].count()
        context['followers_count'] = profile.followers.count()
        context['following_count'] = profile.following.count()

        return context



#  EDIT PROFILE
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/edit_profile.html'

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
    template_name = 'profile/user_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(Profile, user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        context['posts'] = Post.objects.filter(user=profile.user).order_by('-created_at')
        context['posts_count'] = context['posts'].count()
        context['followers_count'] = profile.followers.count()
        context['following_count'] = profile.following.count()

        return context    
    
    
class FollowToggleView(LoginRequiredMixin, View):
    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        target_profile = target_user.profile
        my_profile = request.user.profile

        if target_profile in my_profile.following.all():
            my_profile.following.remove(target_profile)
            followed = False
        else:
            my_profile.following.add(target_profile)
            followed = True

        return JsonResponse({
            'followed': followed,
            'followers_count': target_profile.followers.count()
        })




class LikeToggleView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count()
        })


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        form.instance.user = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('feed')
    

class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"
    
    
class EditPostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['caption']
    template_name = 'profile/edit_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

    def form_valid(self, form):
        messages.success(self.request, "Post edited successfully.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={
            'username': self.request.user.username
        })


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'profile/delete_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={
            'username': self.request.user.username
        })