from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

# Model and Forms
from django.contrib.auth.models import User
from user_auth.models import *
from user_auth.forms import *
from studyapp.views import *
# Create your views here.
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
import openai
from decouple import config
# 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

openai.api_key = SECRET_KEY = config('OPENAI_KEY')



def AiChat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        chatbot_response = generate_response(user_input)
        Chat.objects.create(user=request.user, user_input=user_input, chatbot_response=chatbot_response)
        # return redirect('chat')
    else:
        user_input = ''
        chatbot_response = ''

    chat_history = Chat.objects.filter(user=request.user)

    profile = Profile.objects.get(user=request.user)
    context = {
        'user_input': user_input,
        'chatbot_response': chatbot_response,
        'chat_history': chat_history,
        'profile': profile,
    }
    return render(request, 'ai_chat.html', context)



def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message













def UserProfile(request, username):
    if not request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect("login")
    # user = User.objects.get(username=username)
    user = get_object_or_404(User, username=username)
    # profile = get_object_or_404(Profile, user=user)
    profile = Profile.objects.get(user=user)

    # profile = Profile.objects.get(user__id=user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile.profile_pic = form.cleaned_data.get('profile_pic')
            # profile.profile_banner = form.cleaned_data.get('profile_banner')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.phone = form.cleaned_data.get('phone')
            profile.location = form.cleaned_data.get('location')
            profile.github_url = form.cleaned_data.get('github_url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.twitter_url = form.cleaned_data.get('twitter_url')
            profile.github_url = form.cleaned_data.get('github_url')
            profile.instagram_url = form.cleaned_data.get('instagram_url')
            profile.facebook_url = form.cleaned_data.get('facebook_url')

            profile.save()
            # update_session_auth_hash(request, user)
            url = reverse('profile', kwargs={'username': request.user.username})
            return redirect(url)
            # return HttpResponseRedirect( 'profile' )

    else:
        form = EditProfileForm(instance=request.user.profile)
    template = loader.get_template('profile.html')


   
    context = {
        'form': form,
        'profile': profile

    }
    
    return HttpResponse(template.render(context, request))

@login_required
def update_profile(request):
    # request.session['next'] = request.get_full_path()
    if request.method == 'POST':
        form = EditProfileForm(request.POST or None, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            url = reverse('profile', kwargs = {'username': request.user.username})
            return redirect(url)
    else:
        form = EditProfileForm(instance=request.user.profile)
    template = loader.get_template('edit-profile.html')
    context = {
        'form': form,
    }
    
    return HttpResponse(template.render(context, request))
    # return render(request, 'edit-profile.html', {'form': form})


# def UserProfile(request):
#     template = loader.get_template('work_in_prog.html')


   
#     context = {
        
#     }
    
#     return HttpResponse(template.render(context, request))

def Login(request):
    
    if request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect('dashboard')
   

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if Profile.objects.filter(user=user, first_name__isnull=False, profile_pic__isnull=False).exists():
                    login(request, user)
                    messages.success(request, f"Welcome back {request.user.username}! ")
                    return redirect('dashboard')

                # next = request.session.get('next', '/')
                # return redirect(next)
                else:
                    login(request, user)
                    messages.success(request, f"Welcome back {request.user.username}! ")
                    return redirect('edit-profile')
                
    else:
        messages.error(request, f"Incorrect Username or Password! ")

        form = LoginForm()
        

    template = loader.get_template('authentication/login.html')
    
    context = {
        'form': form

    }
    
    return HttpResponse(template.render(context, request))




def Signup(request):
    request.session['next'] = request.get_full_path()
    if request.user.is_authenticated:
        # return render(request, 'authentication/login.html')
        return redirect('dashboard')

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
            return redirect('edit-profile')

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


# # Chat
# def AiChat(request):

#     template = loader.get_template('ai_chat.html')
    
#     context = {
#         # 'form': form

#     }
    
#     return HttpResponse(template.render(context, request))