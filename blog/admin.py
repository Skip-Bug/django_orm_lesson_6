from django.contrib import admin
from blog.models import Post, Tag, Comment


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_display = ('post', 'author', 'text', 'published_at')


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes')
    list_display = ('title', 'author', 'published_at')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)

# Register your models here
