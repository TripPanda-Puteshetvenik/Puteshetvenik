from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('categories/', include('categories.urls')),
    path('comments/', include('comments.urls')),
    path('ratings/', include('ratings.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
