from django.contrib import admin

from .models import Post, NewsLetter

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'source', 'created_at', 'status', 'validated']
    list_filter = ['validated', 'status', 'created_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    # list_per_page = 10
    
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'ready', 'published']
    

admin.site.register(Post, PostAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)