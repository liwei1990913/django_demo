
from rest_framework import  viewsets
from education.models import UserProfile
from education.serializers import Userserializer

class UserviewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = Userserializer