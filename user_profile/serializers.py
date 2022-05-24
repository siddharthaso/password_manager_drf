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
    id = serializers.IntegerField(label='ID', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), validators=[UniqueValidator(queryset=Profile.objects.all())]),
    location = serializers.CharField(max_length=140)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

#Site Serializer--------------------------------------------------------
class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site    
        fields = ['site_name', 'site_url', 'is_public', 'user']

class SiteSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    site_name = serializers.CharField(max_length=300)
    site_url = serializers.CharField(allow_blank=True, allow_null=True, max_length=300, required=False)
    is_public = serializers.BooleanField(required=False)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        return Site.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.site_name = validated_data.get('site_name', instance.site_name)
        instance.site_url = validated_data.get('site_url', instance.site_url)
        instance.is_public = validated_data.get('is_public', instance.is_public)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance

#Tags Serializer--------------------------------------------------------
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tags_name', 'user']  

class TagsSimpleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    tags_name = serializers.CharField(max_length=300)
    user = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        return Tags.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tags_name = validated_data.get('tags_name', instance.tags_name)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance


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