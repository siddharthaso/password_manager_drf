from django.urls import path,include
# from .views import RegisterView, LoginView
# from . import views

from rest_framework import routers
router = routers.DefaultRouter()

from .views import ProfileViewSet, SiteViewSet, TagsViewSet, TagAPIView, SiteAPIView

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet, names = 'profile')
router.register('sites', SiteViewSet, namespace = 'site')
router.register('tags', TagsViewSet, namespace = 'tag')


urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('APIViewtag/', TagAPIView.as_view(),name="tags"),
    path('APIViewsite/', SiteAPIView.as_view(),name="sites"),
    
    path('router/',include(router.urls)),
]           