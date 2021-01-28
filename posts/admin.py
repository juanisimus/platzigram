from django.contrib import admin



#Models

from posts.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts admin"""
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('title', 'photo')
    search_fields = ('post_user', 'post__prfile', 'post__title',)
    list_filter = ('created', 'modified')

    fieldsets = (
        ('Post', {
        'fields': ('title', 'photo'),
    }),)

    readonly_fields = ('created', 'modified')