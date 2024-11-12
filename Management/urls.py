# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from django.urls import path, include
from sqlalchemy.sql.functions import current_user

from app.models import Task
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart.views import UserViewSet
from app.views import registration
from django.contrib.auth import views as auth_views
from django_email_verification import urls as email_urls
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
]
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


