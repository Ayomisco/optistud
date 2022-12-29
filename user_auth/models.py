from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Username')
    first_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name='Last Name')
        
    phone = models.IntegerField(
         null=True, blank=True, verbose_name='Phone NO.')
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='Location')
    twitter_url = models.URLField(max_length=80, null=True, blank=True)
    github_url = models.URLField(max_length=80, null=True, blank=True)
    facebook_url = models.URLField(max_length=80, null=True, blank=True)
    instagram_url = models.URLField(max_length=80, null=True, blank=True)

    profile_info = models.TextField(max_length=250, null=True, blank=True, verbose_name='About Me')
    created_at = models.DateField(auto_now_add=True)
    # favourites = models.ManyToManyField(Post, verbose_name='Favourite Article')
    profile_pic = models.ImageField(
        upload_to='profile_pictures', blank=True, verbose_name='Picture')
    
    def __str__(self):
        return f"{self.user}, {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"