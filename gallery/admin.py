from django.contrib import admin
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "create_date"]

admin.site.register(Gallery, GalleryAdmin)
