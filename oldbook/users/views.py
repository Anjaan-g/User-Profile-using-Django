from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm, UserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Profile(generic.TemplateView):
    template_name = 'users/profile.html'

class ProfileEdit(generic.TemplateView):
    form_class = UserChangeForm
    success_url = 'profile'
    template_name = 'users/edit_profile.html'
