from rest_framework import serializers
from .models import Profile, Site, Tags
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

#Profile Serializer--------------------------------------------------------
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'location'] #, 'profile_picture'

class ProfileSimpleSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), validators=[UniqueValidator(queryset=Profile.objects.all())]),
    location = serializers.CharField(max_length=140)

#Site Serializer--------------------------------------------------------
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site    
        fields = ['site_name', 'site_url', 'is_public', 'user']

class SiteSimpleSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(max_length=300)
    site_url = serializers.CharField(allow_blank=True, allow_null=True, max_length=300, required=False)
    is_public = serializers.BooleanField(required=False)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)

#Tags Serializer--------------------------------------------------------
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tags_name', 'user']  

class TagsSimpleSerializer(serializers.ModelSerializer):
    tags_name = serializers.CharField(max_length=300)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)


#User Serializer ------------------------------------------------
# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField( max_length=65, min_length=8, write_only=True)
#     email = serializers.EmailField(max_length=255, min_length=4),
#     first_name = serializers.CharField(max_length=255, min_length=2)
#     last_name = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']

#     def validate(self, attrs):
#         email = attrs.get('email', '')
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError(
#                 {'email': ('Email is already in use')})
#         return super().validate(attrs)

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


#Login Serializer ------------------------------------------------
# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(max_length=65, min_length=8, write_only=True)
#     username = serializers.CharField(max_length=255, min_length=2)

#     class Meta:
#         model = User
#         fields = ['username', 'password']