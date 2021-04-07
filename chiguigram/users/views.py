# Django
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, UpdateView
from users.forms import SingupForm

# Models
from django.contrib.auth.models import User
from users.models import Profile

from  posts.models import Post


class LoginView(auth_views.LoginView):
    # Login View
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    # Log out View
    pass


class UserDetailView(DetailView, LoginRequiredMixin):
    # User Detail View
    template_name = 'users/detail.html'
    slug_field = 'username' # Como se hara en la queryset
    slug_url_kwarg = 'username' # Como sera llamado desde la URL
    model = User
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add Users Post to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SingupView(FormView):
    # Sing up view
    template_name = "users/singup.html"
    form_class = SingupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Save form data
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    # Log in view
    template_name = 'users/update/profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'profile_picture']

    def get_object(self, queryset=None):
        # Return users profile if
        return self.request.user.profile

    def get_success_url(self):
        # Return to Users Profile
        username = self.object.user.username
        return reverse('users:detail', kwargs= {'username': username})


