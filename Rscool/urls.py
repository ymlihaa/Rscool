"""Rscool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import  url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import  LogoutView
from django.conf import settings
from django.views.generic import TemplateView
from account.views import router
from django.conf.urls.static import static
urlpatterns = [
       path(
        '',
        auth_views.LoginView.as_view(template_name='page/auth_pages/login.html'),
    ),

# path(
#         'profile/',
#         TemplateView.as_view(template_name='page/profile_page/profile.html'),
#     ),
    path('profile/',router.profileRedirect),
    path('admin/', admin.site.urls),

    url(r'^profile/logout/$', LogoutView.as_view(template_name='page/auth_pages/logout.html'), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
path('djrichtextfield/', include('djrichtextfield.urls'))
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)