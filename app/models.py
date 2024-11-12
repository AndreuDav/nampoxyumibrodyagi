from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy import create_engine


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    assignee = models.CharField(max_length=100, blank=True, null=True)  # Или используйте ForeignKey для пользователей
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
