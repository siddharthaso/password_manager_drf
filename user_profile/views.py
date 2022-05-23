from urllib import response
from rest_framework import viewsets, permissions, status
from .serializers import ProfileSerializer, SiteSerializer, TagsSerializer
from .models import Site,Tags,Profile
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user_profile import serializers

# @csrf_exempt
# class ProfileViewSet (viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     # permission_classes = [permissions.IsAuthenticated]

# class SiteViewSet (viewsets.ModelViewSet):
#     queryset = Site.objects.all()
#     serializer_class = SiteSerializer
#     # permission_classes = [permissions.IsAuthenticated]

# class TagsViewSet (viewsets.ModelViewSet):
#     queryset = Tags.objects.all()
#     serializer_class = TagsSerializer

    # permission_classes = [permissions.IsAuthenticated]

class TagAPIView(ListAPIView):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return self.list(request)

    def get_queryset(self):
        queryset = self.queryset.filter(user = self.request.user)
        # queryset = Site.objects.all().filter(user = self.request.user)
        # if not queryset:
        #    return Response({"msg":"NO DATA"},status=status.HTTP_404_NOT_FOUND)
        return queryset

class SiteAPIView(ListAPIView):
    serializer_class = SiteSerializer
    queryset = Site.objects.all()
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,]

    def get(self,request):
        if self.get_queryset():
            serializer = SiteSerializer(self.get_queryset(),many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"msg":"NO DATA"},status=status.HTTP_404_NOT_FOUND)
    def get_queryset(self):
        queryset = self.queryset.filter(user = self.request.user)
        return queryset













# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
# from .serializers import UserSerializer, LoginSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from django.conf import settings
# from django.contrib import auth
# import jwt
# # Create your views here.


# class RegisterView(GenericAPIView):
#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         username = data.get('username', '')
#         password = data.get('password', '')
#         user = auth.authenticate(username=username, password=password)

#         if user:
#             auth_token = jwt.encode(
#                 {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

#             serializer = UserSerializer(user)

#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)

#             # SEND RES
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)