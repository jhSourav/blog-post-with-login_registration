"""blog URL Configuration

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
from django.contrib import admin
from django.urls import path
from articles.views import article_list,post_detail_view,postCreate
#login ,logout import part
from .views import user_signup,user_login,user_logout #other

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_list, name='article_list'),
    path('<id>', post_detail_view, name='post_detail_view'),
    path('create/', postCreate, name='postCreate'),
#login, logout url part
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
   ]

