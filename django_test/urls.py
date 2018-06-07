"""django_test URL Configuration

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
from education.models import UserProfile


from django.contrib import admin
from django.urls import path,re_path,include
from education import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.acc_login),
    re_path('(\d+)/change', views.test,name='data_change'),
    re_path('(\d+)/delete', views.delete, name='data_delete'),
    path('logout/',  views.acc_logout),
    path('demo/',  views.demo),
    path(r'edu/', include('education.urls')),
    path('add/', views.add_list),
    path('showdata/', views.show_data),
    path('article/',views.article_list),
    path('api/',include('rest_framework.urls')),


]
