
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from django.urls import path
from app import views as user_views
from app.views import registration






urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('user/registration/', registration)
]
