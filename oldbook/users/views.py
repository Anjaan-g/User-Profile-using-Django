from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import CustomUserCreationForm, UserChangeForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Profile(generic.TemplateView):

    template_name = 'users/profile.html'

# class ProfileEdit(generic.CreateView):
#     form_class = EditProfileForm
#     success_url = 'profile'
#     template_name = 'users/edit_profile.html'

# def profile_update_view(request):
#     # obj = get_object_or_404(CustomUser.objects.filter(username = CustomUser.username))
#     form = EditProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     template_name = 'users/edit_profile.html'
#     context = {  "form": form}
#     return render(request, template_name, context)
