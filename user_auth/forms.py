from django.contrib.auth.models import User
from django import forms 
from django.contrib import messages
import requests
# Validation modules
from django.core.exceptions import ValidationError
from django.contrib import messages
from user_auth.models import *


class ChatForm(forms.Form):
    user_input = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input-sm', 'placeholder': 'Type your message here...'}),  max_length=1024)

class SignupForm(forms.ModelForm):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}), max_length=30, required=True)
     email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'form-control form-control-lg'}), max_length=100, required=True)
     password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}), required=True)
     confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}), required=True)


     class Meta:
        model = User
        # message = forms.CharField(widget=CKEditorUploadingWidget())
        fields = ( 'email', 'username', 'password')



     def clean(self):
         super(SignupForm, self).clean()
         password = self.cleaned_data.get('password')
         username = self.cleaned_data.get('username')
         email = self.cleaned_data.get('email')
         
         confirm_password = self.cleaned_data.get('confirm_password')

         # overiding the clean function to make sure password is validate
         if password != confirm_password:
            self._errors['password'] = self.error_class('Password do not match try again')


         forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'master', 'administrator', 
         'root', 'email', 'user', 'join', 'static', 'python']

         if username.lower() in forbidden_users:
            self._errors['username'] = self.error_class('The username you have used is a reserved word...')
         
         if User.objects.filter(email__iexact=email).exists():
            self._errors['email'] = self.error_class('User with this email already exists.')


         return self.cleaned_data


class LoginForm(forms.Form):
     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}), max_length=30, required=True)
     
     password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg'}), required=True)


class EditProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input form-control-lg'
                            }), required=False)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'First Name'}), max_length=50, required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Second Name'}), max_length=50, required=False)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Location'}), max_length=25, required=False)
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control ', 'placeholder': 'phone'}), required=False)
    github_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control ', 'placeholder': 'Github url'}), max_length=200, required=False)
    twitter_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control ', 'placeholder': 'Twitter url'}), max_length=200, required=False)
    facebook_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control ', 'placeholder': 'facebook url'}), max_length=200, required=False)
    instagram_url = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control  form-control-lg', 'placeholder': 'Instagram url'}), max_length=200, required=False)
    
    profile_info = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control', 
                            'placeholder': 'Enter Profile Description', 'rows':3}), max_length=400, required=False)

    class Meta:
        model = Profile
        fields = ('profile_pic', 'first_name', 'last_name','instagram_url','twitter_url',
                  'location',  'profile_info', 'github_url', 'facebook_url')