from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from .models import Comment
from .forms import CommentForm


@login_required
def add_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Коментарът е добавен!')
    return redirect('post_detail', pk=post_pk)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user or request.user.is_staff:
        post_pk = comment.post.pk
        comment.delete()
        messages.success(request, 'Коментарът е изтрит.')
        return redirect('post_detail', pk=post_pk)
    messages.error(request, 'Нямате право да изтривате този коментар.')
    return redirect('post_detail', pk=comment.post.pk)
