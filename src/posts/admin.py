from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'country', 'published', 'created_at', 'views_count']
    list_filter = ['published', 'country__continent', 'travel_types']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body', 'location_name']
