#------------------------------------------------------Function Based View------------------------------------------------------------------------
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from password.models import Passwords
from password.serializers import PasswordModelSerializer, PasswordSimpleSerializer

@csrf_exempt
def password_list(request):
    """
    List all passwords, or create a new password.
    """
    if request.method == 'GET':
        pwds = Passwords.objects.all()
        serializer = PasswordModelSerializer(pwds, many=True)
        return JsonResponse(serializer.data, safe=False)   # 'safe=False' for objects serialization

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PasswordModelSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()       #user=request.user
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
        # serializer.is_valid(raise_exception=True)
        # serializer.save(user=request.user)
        # return JsonResponse(serializer.data, status=201)

@csrf_exempt
def password_detail(request, pk):
    """
    Retrieve, update or delete a password.
    """
    try:
        pwd = Passwords.objects.get(pk=pk)
    except pwd.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PasswordModelSerializer(pwd)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        #if not put instance then it will create new instance when .save() called
        serializer = PasswordModelSerializer(pwd, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pwd.delete()
        return HttpResponse(status=204)


#------------------------------------------------------Function Based API View Using decorator ------------------------------------------------------------------------
from rest_framework import status
from rest_framework.response import Response
from password.models import Passwords
from password.serializers import PasswordModelSerializer, PasswordSimpleSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def password_list_decorator(request):

    if request.method == 'GET':
        pwds = Passwords.objects.all()
        serializer = PasswordModelSerializer(pwds, many=True)
        return Response(serializer.data)

        # title = request.query_params.get('title', None)
        # if title is not None:
        #     tutorials = tutorials.filter(title__icontains=title)

    elif request.method == 'POST':
        serializer = PasswordModelSerializer(data=request.data)
        import pdb; pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Passwords.objects.all().delete()
        return Response({'message': 'f{count[0]} Passwords were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def password_detail_decorator(request, pk):
    
    try: 
        pwd = Passwords.objects.get(pk=pk) 
    except Passwords.DoesNotExist: 
        return Response({'message': 'The password does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        serializer = PasswordModelSerializer(pwd) 
        return Response(serializer.data) 

    elif request.method == 'PUT': 
        serializer = PasswordModelSerializer(pwd, data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        pwd.delete() 
        return Response({'message': 'password was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


#------------------------------------------------------class Based View using APIView------------------------------------------------------------------------
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from password.models import Passwords
from password.serializers import PasswordModelSerializer, PasswordSimpleSerializer

# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

class PasswordListAPIView(APIView):
    """
    View to list all passwords.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        passwords = Passwords.objects.all()
        serializer = PasswordModelSerializer(passwords, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PasswordModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordDetailAPIView(APIView):
    """
    Retrieve, update or delete a password instance.
    """
    def get_object(self, pk):
        try:
            return Passwords.objects.get(pk=pk)
        except Passwords.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pwd = self.get_object(pk)
        serializer = PasswordModelSerializer(pwd)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pwd = self.get_object(pk)
        serializer = PasswordModelSerializer(pwd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pwd = self.get_object(pk)
        pwd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#------------------------------------------------------Class Based View using GenericAPIView------------------------------------------------------------------------

from .models import Passwords
from .serializers import PasswordModelSerializer, PasswordSimpleSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters

class PasswordListGenAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['password']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PasswordDetailGenAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

from django_filters.rest_framework import DjangoFilterBackend

class PasswordListGenericAPIView(generics.ListCreateAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['password', 'tag']

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        pwd = self.kwargs.get('pwd',None)
        print(**self.kwargs)
        if pwd:
            return Passwords.objects.filter(password__strartswith=pwd)# or Passwords.objects.all()
        return Passwords.objects.all()

class PasswordDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer

#------------------------------------------------------MOdelViewset------------------------------------------------------------------------

from rest_framework import permissions
from rest_framework import viewsets
from .serializers import PasswordModelSerializer
from .models import Passwords
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class PasswordModelViewSet (viewsets.ModelViewSet):
    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['password', 'id']
    ordering = ['id']