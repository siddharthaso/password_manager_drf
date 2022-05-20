from django.urls import path
# from .views import RegisterView, LoginView
from . import views


urlpatterns = [
    # path('', views.HomeView.as_view(), name="home"),
    # path('register/', RegisterView.as_view()),
    # path('login/', LoginView.as_view()),
    path('tag/',views.TagAPIView.as_view(),name="tags"),
    path('site/',views.SiteAPIView.as_view(),name="sites")
]           