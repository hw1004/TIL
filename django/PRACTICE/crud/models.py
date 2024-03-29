from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# User = get_user_model()
AUTH_USER_MODEL = 'User'

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    major = models.CharField(max_length=10)
    description = models.TextField()
    # Timestamp => 생성시간/수정시간
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Reply(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    rank = models.IntegerField()
    
