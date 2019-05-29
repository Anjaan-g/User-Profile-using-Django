from django.urls import path
from . import views
# from .views import profile_update_view

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.Profile.as_view(), name='profile'),
    # path('profile/edit',profile_update_view)
]
