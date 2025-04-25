from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)
    ROLE_CHOICES = (
        ('normal', '일반 사용자'),
        ('premium', '프리미엄 사용자'),
        ('admin', '관리자'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='normal')
