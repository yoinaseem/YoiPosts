"""CSWebApp URL Configuration

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog.views import cs_blog_home_view, about_view, home_view
from music.views import mz_blog_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="site_home"),
    path('blog/', cs_blog_home_view, name="blog_home"),
    path('about/', about_view, name="blog_about"),
    path('music/', mz_blog_home_view, name="music_blog"),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
