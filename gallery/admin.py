from django.contrib import admin
from .models import Gallery, ImageNews

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "create_date"]

class ImageNewsAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "create_date"]

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ImageNews, ImageNewsAdmin)