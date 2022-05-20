from rest_framework import serializers
from .models import Passwords
# from django.contrib.auth.models import User
# from user_profile.models import Site, Tags

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passwords
        fields = '__all__'  

# class PasswordSerializer(serializers.Serializer):
#     user = serializers.ForeignKey(User)
#     password = serializers.CharField(max_length=200, null=False)
#     description = serializers.TextField(max_length=100, null=True, blank=True)
#     email = serializers.CharField(max_length=200)
#     site = serializers.ForeignKey(Site, null=True, blank=True, related_name = 'passwords')
#     category = serializers.CharField(max_length=300, null=True)
#     tag = serializers.ForeignKey(Tags, null= True, blank =True, related_name = 'passwords')
#     serializers.