from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email' )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

# class EditProfileForm(UserChangeForm):
#     username = CustomUser.username
#     email = CustomUser.email
#     image = CustomUser.image
#
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'image')

    # def clean_email(self, *args, **kwargs):
    #     instance = self.instance
    #     email = self.cleaned_data.get('email')
    #     qs = CustomUser.objects.filter(email__iexact = email)
    #     if instance is not None:
    #         qs = qs.exclude(pk=instance.pk)
    #     if qs.exists():
    #         raise forms.ValidationError("This email is already taken.")
    #     return email
