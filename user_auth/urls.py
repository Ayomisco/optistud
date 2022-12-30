from django.urls import path
from user_auth.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', Signup, name='signup'),
    path('login/', Login, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('logout/', logout_view, name='logout'),
    # path('profile/edit/', EditProfile, name='edit-profile'),
]