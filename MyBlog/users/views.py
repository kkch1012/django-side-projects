from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post
from users.decorators import role_required

def login_view(request):
    return render(request, "users/login.html")
@role_required("admin")
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("posts:feed")  # or wherever your post list is

@login_required
def profile_view(request):
    return render(request, "users/profile.html", {
        "user": request.user,
        "my_posts": Post.objects.filter(user=request.user)
    })