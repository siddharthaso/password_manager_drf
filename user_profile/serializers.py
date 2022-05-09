from rest_framework import serializers
from .models import Profile, Site, Tags

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'profile_picture', 'location'] 

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site    
        fields = ['site_name', 'site_url', 'is_public', 'user']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tags_name', 'user']