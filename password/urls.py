from django.urls import path
from . import views

#http://127.0.0.1:8000/
urlpatterns = [
    path('passwords/', views.password_list),
    path('passwords/<int:pk>/', views.password_detail),
    # path('passwords/', views.view_password, name="view_password"),
    # path('passwords/', views.Password, name="view_password"),
]