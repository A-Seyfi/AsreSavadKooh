from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('users.urls')),
    path('', views.home, name='home_page'),
    path('admin/', admin.site.urls),
    path('world/', views.world),
    path('article/', views.article),
    path('404/', views.custom_404_page),
]
