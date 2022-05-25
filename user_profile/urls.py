from django.urls import path,include
# from .views import RegisterView, LoginView
# from . import views

from rest_framework import routers
router = routers.DefaultRouter()

from .views import ProfileModelViewSet, SiteModelViewSet, TagsModelViewSet, TagAPIView, SiteAPIView

router = routers.DefaultRouter()
router.register('profiles', ProfileModelViewSet)
router.register('sites', SiteModelViewSet)
router.register('tags', TagsModelViewSet)


urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('APIViewtag/', TagAPIView.as_view(),name="tags"),
    path('APIViewsite/', SiteAPIView.as_view(),name="sites"),
    
    #modelviewset
    path('router/',include(router.urls)),
]           