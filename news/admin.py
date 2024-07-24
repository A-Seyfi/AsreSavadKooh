from django.contrib import admin
from .models import Category, Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "created_at"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["article", "user", "text", "create_date"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)