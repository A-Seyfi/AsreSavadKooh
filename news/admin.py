from django.contrib import admin
from .models import Category, Article, Comment, Gallery

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "author", "created_at"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "user", "text", "create_date"]

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "create_date"]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category)