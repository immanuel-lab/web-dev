"""djproject URL Configuration

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
from django.urls import path,include
from api1.views import EmployeeList
from rest_framework.urlpatterns import format_suffix_patterns
from api1 import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')), 

    path('oauth/', include('social_django.urls', namespace='social')),
    path('employees/',views.EmployeeList.as_view(),name='employees'),
    path('api/token/',obtain_auth_token,name='obtain'),
    path('news',views.news,name='news'),

# donation
 path('donation/', views.index, name="donation"),
    path('charge/', views.charge, name="charge"),
    path('success/', views.successMsg, name="success"),

]
