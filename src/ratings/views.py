from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from posts.models import Post
from .models import Rating
from .forms import RatingForm


@login_required
def add_rating(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if post.author == request.user:
        messages.error(request, 'Не можете да оценявате собствения си пътепис.')
        return redirect('post_detail', pk=post_pk)

    existing = Rating.objects.filter(post=post, user=request.user).first()
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=existing)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.user = request.user
            rating.save()
            messages.success(request, 'Оценката е записана!')
    return redirect('post_detail', pk=post_pk)
