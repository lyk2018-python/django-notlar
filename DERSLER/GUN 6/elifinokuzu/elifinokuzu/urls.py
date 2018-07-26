"""elifinokuzu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from dictionary import views as dictionary_views
from accounts import views as account_views

urlpatterns = [
    path('', dictionary_views.home, name="home"),
    path('about/', dictionary_views.about, name="about"),
    path('support/', dictionary_views.support, name="support"),
    path('node/<int:id>/', dictionary_views.node_detail, name="node_detail"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', account_views.signup, name='signup'),
    path('accounts/profile/', account_views.dashboard, name='dashboard' ),
	path('submit/', dictionary_views.submit, name='submit')
]
