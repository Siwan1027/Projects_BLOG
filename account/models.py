# account/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from board.models import Posting
# Create your models here.

class User(AbstractUser):
    like_postings = models.ManyToManyField(Posting, related_name='like_users')
    follow = models.ManyToManyField('self' , symmetrical = False, related_name = 'follower')