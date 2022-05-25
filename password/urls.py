from django.urls import path, include
from . import views

from .views import PasswordModelViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('',PasswordModelViewSet)

#http://127.0.0.1:8000/
urlpatterns = [
    path('func/', views.password_list),
    path('func/<int:pk>/', views.password_detail),
    # path('passwords/', views.view_password, name="view_password"),
    # path('passwords/', views.Password, name="view_password"),

    path('modelviewset/',include(router.urls)),
]