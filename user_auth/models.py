from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# compressing images
from io import BytesIO
from PIL import Image
from django.core.files import File
import cloudinary
from django.conf import settings
# Create your models here.

# def compress(profile_pic):
#     im = Image.open(profile_pic)
#     im_io = BytesIO() 
#     im.save(im_io, 'JPEG', quality=60) 
#     new_image = File(im_io, name=profile_pic.name)
#     return new_image

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

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)    # user = models.fore
    user_input = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_input}, {self.timestamp}"

    class Meta:
        # ordering = ['-timestamp']
        verbose_name = "Chat"
        verbose_name_plural = "Chats"