from django.contrib import admin
from .models import Article,Comment
from .models import Image
admin.site.register(Image)
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, PostAdmin)