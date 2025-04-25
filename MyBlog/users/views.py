from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from posts.models import Post
from users.decorators import role_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")  # 로그인 성공 시 이동할 페이지
        else:
            messages.error(request, "아이디 또는 비밀번호가 올바르지 않습니다.")
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

def logout_view(request):
    logout(request)
    return redirect("login")