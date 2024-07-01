from django.views.generic import ListView, DetailView
from .models import Article

class homeListView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        myset = {
            "urgent" : Article.objects.filter(is_urgent=True),
            "world" : Article.objects.filter(category__url_title="world"),
            "politics" : Article.objects.filter(category__url_title="politics"),
            "economy" : Article.objects.filter(category__url_title="economy"),
            "sport" : Article.objects.filter(category__url_title="sport"),
            "local" : Article.objects.filter(category__url_title="local"),
            "science" : Article.objects.filter(category__url_title="science"),
            "travel" : Article.objects.filter(category__url_title="travel"),
            "health" : Article.objects.filter(category__url_title="health"),
            "style" : Article.objects.filter(category__url_title="style"),
            "weather" : Article.objects.filter(category__url_title="weather"),
            "world" : Article.objects.filter(category__url_title="gallery"),
        }
        return myset


class WorldListView(ListView):
    template_name = 'news/world.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    
    def get_queryset(self):
        return Article.objects.filter(category__url_title="world")

class PoliticsListView(ListView):
    template_name = 'news/politics.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="politics")

class EconomyListView(ListView):
    template_name = 'news/economy.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="economy")

class SportListView(ListView):
    template_name = 'news/sport.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="sport")

class LocalListView(ListView):
    template_name = 'news/local.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="local")

class ScienceListView(ListView):
    template_name = 'news/science.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="science")

class TravelListView(ListView):
    template_name = 'news/travel.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="travel")

class HealthListView(ListView):
    template_name = 'news/health.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="health")

class StyleListView(ListView):
    template_name = 'news/style.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="style")

class WeatherListView(ListView):
    template_name = 'news/weather.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="weather")

class GalleryListView(ListView):
    template_name = 'news/gallery.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(category__url_title="gallery")

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article.html'
    context_object_name = 'news'
