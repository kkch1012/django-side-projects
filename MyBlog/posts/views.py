from django.shortcuts import render, get_object_or_404
from .models import Post
from users.decorators import role_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "posts/list.html", {"posts": posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "posts/detail.html", {"post": post})


@role_required("admin")
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("posts:list")

@login_required
def my_posts(request):
    posts = Post.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "posts/my_posts.html", {"posts": posts})


def search_board(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        posts = Post.objects.none()
    return render(request, "posts/search.html", {"posts": posts})