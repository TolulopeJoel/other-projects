from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    model = Post
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'status', 'author',)
    list_filter = ('created_at',)


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('body', 'author', 'created_at',)
    list_filter = ('created_at',)


admin.site.register(Comment, CommentAdmin)
