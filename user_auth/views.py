from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

# Model and Forms
from django.contrib.auth.models import User
from django.urls import reverse
from user_auth.models import *
from user_auth.forms import *
from studyapp.views import *
# Create your views here.
from django.contrib.auth import authenticate, login

def UserProfile(request, username):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    # user = User.objects.get(username=username)
    user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(Profile, user=user)
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, request.FILES, instance=profile)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            # profile.profile_banner = form.cleaned_data.get('profile_banner')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.github_url = form.cleaned_data.get('github_url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.twitter_url = form.cleaned_data.get('phone')
            profile.github_url = form.cleaned_data.get('twitter_url')
            profile.instagram_url = form.cleaned_data.get('instagram_url')
            profile.facebook_url = form.cleaned_data.get('facebook_url')

            profile.save()
            # update_session_auth_hash(request, user)
            # return redirect('profile')
            return HttpResponseRedirect( 'profile')

    else:
        form = EditProfileForm(instance=profile)
    template = loader.get_template('profile.html')


   
    context = {
        'form': form,
        'profile': profile

    }
    return HttpResponse(template.render(context, request))

def edit_profile(request, username):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    # user = User.objects.get(username=username)
    user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(Profile, user=user)
    profile = Profile.objects.get(user=user)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, request.FILES, instance=profile)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            # profile.profile_banner = form.cleaned_data.get('profile_banner')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.github_url = form.cleaned_data.get('github_url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.twitter_url = form.cleaned_data.get('phone')
            profile.github_url = form.cleaned_data.get('twitter_url')
            profile.instagram_url = form.cleaned_data.get('instagram_url')
            profile.facebook_url = form.cleaned_data.get('facebook_url')

            profile.save()
            # update_session_auth_hash(request, user)
            # return redirect('profile')
            return HttpResponseRedirect( f'profile')

    else:
        form = EditProfileForm(instance=profile)
        template = loader.get_template('edit-profile.html')


   
    context = {
        'form': form,
        'profile': profile

    }
    return HttpResponse(template.render(context, request))

# class UserProfile(DetailView):
#     model = Profile
#     template_name = 'profile.html'
#     slug_field = "user__username"

def Login(request):
    
    if request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect('index')
   

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back {request.user.username}! ")
                url = reverse(f'index')
                return HttpResponseRedirect(url)
                
    else:
        print('error')
        form = LoginForm()

    template = loader.get_template('authentication/login.html')
    
    context = {
        'form': form

    }
    
    return HttpResponse(template.render(context, request))




def Signup(request):
    if request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect('index')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, f"Account Created Successfully, {request.user.username}! ")
            return redirect('index')

    else:
        form = SignupForm()


    template = loader.get_template('authentication/signup.html')

    context = {
        'form': form,

    }

    # return render(request, 'signup.html', context)
    return HttpResponse(template.render(context, request))


def logout_view(request):
    logout(request)
    return redirect('login')