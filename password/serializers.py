from rest_framework import serializers
from .models import Passwords
from django.contrib.auth.models import User
from user_profile.models import Site, Tags

#Password Serializer--------------------------------------------------------
class PasswordModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passwords
        fields = '__all__'  

class PasswordSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    password = serializers.CharField(max_length=200)
    description = serializers.CharField(allow_blank=True, allow_null=True, max_length=100, required=False, style={'base_template': 'textarea.html'})
    email = serializers.CharField(max_length=200)
    # category = serializers.CharField(allow_null=True, choices=[('ENT', 'Entertainment'), ('LER', 'Learning'), ('SHO', 'Shopping'), ('PAY', 'Payment')], required=False)
    category = serializers.ChoiceField(allow_null=True, choices=['ENT', 'LER', 'SHO', 'PAY'], required=False)
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    site = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Site.objects.all(), required=False)
    tag = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Tags.objects.all(), required=False)

    def create(self, validated_data):
        return Passwords.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.category = validated_data.get('category', instance.category)
        instance.user = validated_data.get('user', instance.user)
        instance.site = validated_data.get('site', instance.site)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance