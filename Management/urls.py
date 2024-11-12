<<<<<<< HEAD
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from sqlalchemy.sql.functions import current_user

from app.models import Task
=======
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart.views import UserViewSet
>>>>>>> 1a703353dbb6626a4b7ea24d946cff5cf1ec1a8e
from app.views import registration
from django.contrib.auth import views as auth_views
from django_email_verification import urls as email_urls
<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('user/registration/', registration),
    path('admin/', admin.site.urls),
=======

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
>>>>>>> 1a703353dbb6626a4b7ea24d946cff5cf1ec1a8e
    path('user/registration/', registration),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('email/', include(email_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

