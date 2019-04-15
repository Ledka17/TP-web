"""askme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

# Здесь зранятся пути, которые будут отображаться при запросе на определенную страницу

from django.contrib import admin
from django.urls import path, re_path

from asker import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path(r'login/', views.login, name='login'),
    path(r'hot/', views.hot, name='hot'),
    path(r'tag/<qtag>/', views.tag, name='tag'),
    path(r'ask/', views.ask, name='ask'),
    path(r'signup/', views.signup, name='signup'),
    path(r'question/<int:qid>/', views.question, name='question'),
    path(r'<name>/settings/', views.settings, name='settings'),
]
