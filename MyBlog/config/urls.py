from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config.views import index
from posts.views import search_board

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("posts/", include("posts.urls")),
    path("comments/", include("comments.urls")),
    path("", include("users.urls")),  # 로그인/프로필 경로는 users.urls에서 관리
    path("search/", search_board, name="search"),
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
