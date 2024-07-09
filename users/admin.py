from django.contrib import admin
from .models import UserProfile

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "email"]

admin.site.register(UserProfile, UserAdmin)