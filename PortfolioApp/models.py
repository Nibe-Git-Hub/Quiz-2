from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    project_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    portfolio_title = models.CharField(max_length=255)
    portfolio_description = models.TextField(blank=True)
    project = models.OneToOneField(Project, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Portfolio"