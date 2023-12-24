from django.views.generic import CreateView
from users.models import User
from users.forms import UserRegisterForm


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
