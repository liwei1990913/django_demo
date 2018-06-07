from rest_framework import routers,serializers,viewsets
from education.rest_views import Userserializer,UserviewSet
from education import views
router=routers.DefaultRouter()
router.register(r'user',UserviewSet)
from django.urls import path,re_path,include

urlpatterns = [

    path('api/',include(router.urls) ),

    path('city/',views.city ),
    path('province/',views.province ),
    re_path('city_(\d+)/', views.city1),
    re_path('county_(\d+)/', views.county),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))

]
