from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Post
from .forms import PostForm, GalleryFormSet
from gallery.models import GalleryImage
from comments.forms import CommentForm
from ratings.forms import RatingForm
from ratings.models import Rating


def home(request):
    posts = Post.objects.filter(published=True).select_related('author', 'country__continent')
    search = request.GET.get('q', '')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search) |
            Q(location_name__icontains=search)
        )
    featured = posts[:3]
    recent = posts[3:9]
    return render(request, 'posts/home.html', {
        'featured': featured,
        'recent': recent,
        'search': search,
        'all_posts': posts,
    })


def post_list(request):
    posts = Post.objects.filter(published=True).select_related('author', 'country__continent')
    search = request.GET.get('q', '')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search) |
            Q(location_name__icontains=search)
        )
    return render(request, 'posts/post_list.html', {'posts': posts, 'search': search})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    post.views_count += 1
    post.save(update_fields=['views_count'])

    gallery = post.gallery_images.all()
    comments = post.comments.select_related('author__profile').all()
    comment_form = CommentForm()
    rating_form = RatingForm()
    avg_rating = post.get_avg_rating()
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(post=post, user=request.user).first()
        if user_rating:
            rating_form = RatingForm(instance=user_rating)

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'gallery': gallery,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'avg_rating': avg_rating,
        'user_rating': user_rating,
    })


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        formset = GalleryFormSet(request.POST, request.FILES, queryset=GalleryImage.objects.none())
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            for f in formset:
                if f.cleaned_data.get('image') and not f.cleaned_data.get('DELETE'):
                    img = f.save(commit=False)
                    img.post = post
                    img.save()
            messages.success(request, 'Пътеписът е публикуван!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        formset = GalleryFormSet(queryset=GalleryImage.objects.none())
    return render(request, 'posts/post_form.html', {'form': form, 'formset': formset, 'action': 'Нов'})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        formset = GalleryFormSet(request.POST, request.FILES, queryset=post.gallery_images.all())
        if form.is_valid() and formset.is_valid():
            form.save()
            for f in formset:
                if f.cleaned_data.get('image') and not f.cleaned_data.get('DELETE'):
                    img = f.save(commit=False)
                    img.post = post
                    img.save()
                elif f.cleaned_data.get('DELETE') and f.instance.pk:
                    f.instance.delete()
            messages.success(request, 'Пътеписът е обновен!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        formset = GalleryFormSet(queryset=post.gallery_images.all())
    return render(request, 'posts/post_form.html', {'form': form, 'formset': formset, 'post': post, 'action': 'Редактиране'})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Пътеписът е изтрит.')
        return redirect('home')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
