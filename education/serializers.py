from rest_framework import serializers
from education.models import UserProfile, LANGUAGE_CHOICES, STYLE_CHOICES


class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UserProfile
        fields=('url','email','name','is_staff')
