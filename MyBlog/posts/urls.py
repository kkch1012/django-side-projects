from django.urls import path
from .views import post_list, post_detail, delete_post, my_posts, search_board

app_name = "posts"

urlpatterns = [
    path("", post_list, name="list"),
    path("<int:post_id>/", post_detail, name="detail"),
    path("<int:post_id>/delete/", delete_post, name="delete"),
    path("mine/", my_posts, name="mine"),
    path("search/", search_board, name="search"),
]
