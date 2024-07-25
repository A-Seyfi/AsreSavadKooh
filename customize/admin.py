from django.contrib import admin
from .models import AboutUs, Links, Address

class AboutAdmin(admin.ModelAdmin):
    list_display = ["phone_number", "email"]

class LinksAdmin(admin.ModelAdmin):
    list_display = ["insta_urls", "rubika_urls"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["city", "post_code"]

admin.site.register(AboutUs, AboutAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(Address, AddressAdmin)