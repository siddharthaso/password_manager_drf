from django.contrib import admin
from django.urls import path,include

from password.views import PasswordViewSet
from user_profile.views import ProfileViewSet, SiteViewSet, TagsViewSet

from rest_framework import routers
router = routers.DefaultRouter()

router.register('passwords',PasswordViewSet)
router.register('profiles', ProfileViewSet)
router.register('sites', SiteViewSet)
router.register('tags', TagsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user_profile.urls')),
    path('',include('password.urls')),
    path('',include(router.urls)),
]


