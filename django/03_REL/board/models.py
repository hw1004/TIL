from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Article(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # user 데이터가 사라진다면 그에 해당되는 Article 다 삭제
    
    # SQL) VARCHAR
    title = models.CharField(max_length=200)
    # SQL) TEXT
    content = models.TextField()
    # Timestamp => 생성시간/수정시간
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User, related_name='like_articles')
    
    
# 1. app => board
# 2. model => Article
# 3. id, title(VARCHAR 200), content(TextField)

class Comment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='friends')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)