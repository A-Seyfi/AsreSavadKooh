from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeListView.as_view(), name='home_page'),
    path('world/', views.WorldListView.as_view(), name='world-page'),
    path('politics/', views.PoliticsListView.as_view(), name='politics-page'),
    path('economy/', views.EconomyListView.as_view(), name='economy-page'),
    path('sport/', views.SportListView.as_view(), name='sport-page'),
    path('local/', views.LocalListView.as_view(), name='local-page'),
    path('science/', views.ScienceListView.as_view(), name='science-page'),
    path('travel/', views.TravelListView.as_view(), name='travel-page'),
    path('health/', views.HealthListView.as_view(), name='health-page'),
    path('style/', views.StyleListView.as_view(), name='style-page'),
    path('weather/', views.WeatherListView.as_view(), name='weather-page'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery-page'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail'),
]