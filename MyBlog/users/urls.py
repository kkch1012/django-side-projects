from django.urls import path
from users.views import login_view, profile_view  # 필요한 뷰들 import

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
]
