from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('users.urls')),
    path('', include('news.urls')),
    path('home/about-us/', include('customize.urls')),
    path('gallery', include('gallery.urls')),
]
