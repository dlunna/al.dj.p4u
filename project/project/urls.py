"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
from django.urls import include
from django.conf.urls.i18n import i18n_patterns
#from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('message', views.message, name='message'),
    path('contact/', views.contact, name='contact'),
    path('simple/', views.simple, name='simple'),

    #prefix_default_language=False,
]

urlpatterns += i18n_patterns (

    #path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),

    #prefix_default_language=False,
)


