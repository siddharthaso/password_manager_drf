from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view),
    path('user/',include('user_profile.urls')),
    path('password/',include('password.urls')),

	path('api/token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
	path('api/token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
]