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
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        # import pdb; pdb.set_trace()
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


#------------------------------------------------------Function Based View Using ------------------------------------------------------------------------






#------------------------------------------------------class Based View------------------------------------------------------------------------

from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all passwords.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all passwords.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

#------------------------------------------------------Function Based View------------------------------------------------------------------------

#------------------------------------------------------MOdelViewset------------------------------------------------------------------------

from rest_framework import permissions
from rest_framework import viewsets
from .serializers import PasswordModelSerializer
from .models import Passwords

class PasswordModelViewSet (viewsets.ModelViewSet):
    queryset = Passwords.objects.all()
    serializer_class = PasswordModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status
# from tutorials.models import Tutorial
# from tutorials.serializers import TutorialSerializer
# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
#         title = request.query_params.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try: 
#         tutorial = Tutorial.objects.get(pk=pk) 
#     except Tutorial.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
#     if request.method == 'GET': 
#         tutorial_serializer = TutorialSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)