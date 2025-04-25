from django.shortcuts import redirect, get_object_or_404
from .models import Comment
from posts.models import Post
from users.decorators import role_required
from django.http import HttpResponseForbidden

@role_required("premium")
def create_comment(request, post_id):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                user=request.user,
                post_id=post_id,
                content=content
            )
    return redirect("posts:detail", post_id=post_id)

@role_required("premium")
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # 댓글 작성자 본인이거나 관리자만 수정 가능
    if comment.user != request.user and request.user.role != "admin":
        return HttpResponseForbidden("수정 권한이 없습니다.")

    if request.method == "POST":
        comment.content = request.POST.get("content")
        comment.save()
        return redirect("posts:detail", post_id=comment.post.id)

    # GET 요청 시 수정 폼 보여주기 (선택사항, 나중에 구현 가능)
    return HttpResponseForbidden("잘못된 접근입니다.")

@role_required("premium")
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # 댓글 작성자 본인 또는 관리자만 삭제 가능
    if comment.user != request.user and request.user.role != "admin":
        return HttpResponseForbidden("삭제 권한이 없습니다.")

    post_id = comment.post.id
    comment.delete()
    return redirect("posts:detail", post_id=post_id)