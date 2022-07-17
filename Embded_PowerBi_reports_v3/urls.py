"""Embded_PowerBi_reports_v3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from user_login import views as user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashbord.urls') ),
    # path('login/', include('user_login.urls'))
    path("login/",user.user_login,name='login'),
    path("logout/",user.user_logout,name='logout'),
    path('steps_for_register_one/', user.register_steps, name='register'),
    path('steps_for_register_two/', user.register_steps2, name='register2'),
    path('register/',user.registre,name="registre_me"),
    path('add_user/',user.add,name="validate"),
    
    path("redirect_url/",user.termi,name='termi'),
    # path("logout/",auth_view.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
]
