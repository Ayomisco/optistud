"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# Media Files
from django.conf.urls.static import static
from django.conf import settings
from user_auth.views import *

urlpatterns = [
    path('optimum-admin/', admin.site.urls),
    path('', include('studyapp.urls')),
    path('account/', include('user_auth.urls')),
    # re_path(r'^(profile/?P\<username>\w+)/$',UserProfile, name='profile'),
    path('profile/', UserProfile, name='profile'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Optimum Admin"
admin.site.site_title = "Optimum Study Admin Portal"
admin.site.index_title = "Welcome to Optimum Admin Website"

handler404 = 'studyapp.views.error_404'
handler500 = 'studyapp.views.error_500'



