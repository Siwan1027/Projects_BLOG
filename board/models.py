# board/models.py
from django.db import models
from django.conf import settings

# Create your models here.

class Posting(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add= True)
    # Get User info
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Get Posting info
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)