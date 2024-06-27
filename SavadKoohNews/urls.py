from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', views.home),
    path('article/', views.article),
    path('404/', views.custom_404_page),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('forgot/', views.forgot_pass),
    path('reset/', views.reset_pass)
]
