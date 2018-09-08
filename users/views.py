from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView
from users.models import User
from django.urls import reverse_lazy, reverse
from users.mixins import ProfileAccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from users.forms import UserSignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


# Create your views here.

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'

class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username')
    template_name = 'profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.object.pk])


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    pass

class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('tuites:post_tuite') 

class FollowersListView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        request_user = self.request.user

        followers = request_user.following.filter(pk=user_pk).exists()

        if followers:
            request_user.following.remove(user)
        else:
            request_user.following.add(user)

        return reverse('users:profile', args=[user_pk])
