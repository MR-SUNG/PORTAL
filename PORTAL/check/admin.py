from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['auto_increment_id', 'is_status', 'kind', 'content', 'create_at', 'update_at']
	list_display_links = ['content']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['message','create_at']
	list_display_links = ['message']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_display_links = ['name']