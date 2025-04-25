from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
    (None, {"fields": ("username", "password")}),
    ("개인정보", {"fields": ("first_name", "last_name", "email")}),
    ('추가 정보', {'fields': ('profile_image', 'short_description', 'role')}),
     (
         "권한",
         {
             "fields": (
                 "is_active",
                 "is_staff",
                 "is_superuser",
             )
         },
     ),
     ("중요한 일정", {"fields": ("last_login", "data_joined")}),
     ]

