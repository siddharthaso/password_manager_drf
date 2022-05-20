from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view

# from password.views import PasswordViewSet
from user_profile.views import ProfileViewSet, SiteViewSet, TagsViewSet

from rest_framework import routers


schema_view = get_swagger_view(title='Pastebin API')
router = routers.DefaultRouter()

# router.register('passwords',PasswordViewSet)
router.register('profiles', ProfileViewSet)
# router.register('sites', SiteViewSet)
# router.register('tags', TagsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('',include('user_profile.urls')),
    path('',include('password.urls')),
    path('api/',include(router.urls)),
]
