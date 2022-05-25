from django.urls import path, include
from . import views

# from .views import PasswordModelViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',views.PasswordModelViewSet)

#http://127.0.0.1:8000/
urlpatterns = [
    path('func/', views.password_list),
    path('func/<int:pk>/', views.password_detail),

    path('funcDecorator/', views.password_list_decorator),
    path('funcDecorator/<int:pk>/', views.password_detail_decorator),

    path('classAPIView/', views.PasswordListAPIView.as_view()),
    path('classAPIView/<int:pk>/', views.PasswordDetailAPIView.as_view()),

    path('classAPIView/', views.PasswordListAPIView.as_view()),
    path('classAPIView/<int:pk>/', views.PasswordDetailAPIView.as_view()),

    path('classGenAPIView/', views.PasswordListGenAPIView.as_view()),
    path('classGenAPIView/<int:pk>/', views.PasswordDetailGenAPIView.as_view()),

    path('classGenericAPIView/', views.PasswordListGenericAPIView.as_view()),
    path('classGenericAPIView/<int:pk>/', views.PasswordDetailGenericAPIView.as_view()),

    path('modelviewset/',include(router.urls)),
]