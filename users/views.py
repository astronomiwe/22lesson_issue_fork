from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm

from django.contrib.auth import logout
from django.shortcuts import redirect


def logout_view(request):
    logout(request)
    return redirect('/')

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    succes_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
