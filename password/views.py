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
#------------------------------------------------------Function Based View------------------------------------------------------------------------

# from rest_framework import viewsets
# from .serializers import PasswordSerializer
# from .models import Passwords

# class PasswordViewSet (viewsets.ModelViewSet):
#     queryset = Passwords.objects.all()
#     serializer_class = PasswordSerializer