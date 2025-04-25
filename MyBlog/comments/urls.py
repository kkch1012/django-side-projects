from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("create/<int:post_id>/", views.create_comment, name="create"),
    path("edit/<int:comment_id>/", views.edit_comment, name="edit"),
    path("delete/<int:comment_id>/", views.delete_comment, name="delete"),
]
