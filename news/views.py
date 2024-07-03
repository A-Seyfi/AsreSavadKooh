from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Article, Comment

class homeListView(ListView):
    template_name = 'index.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']

    def get_queryset(self):
        myset = {
            "urgent1" : Article.objects.filter(is_urgent=True).order_by('-id')[:1],
            "urgent2" : Article.objects.filter(is_urgent=True).order_by('-id')[1:2],
            "urgent3" : Article.objects.filter(is_urgent=True).order_by('-id')[2:3],
            "urgent4" : Article.objects.filter(is_urgent=True).order_by('-id')[3:4],
            "world" : Article.objects.filter(category__url_title="world").order_by('-id')[:4],
            "politics" : Article.objects.filter(category__url_title="politics").order_by('-id')[:4],
            "economy" : Article.objects.filter(category__url_title="economy").order_by('-id')[:4],
            "sport" : Article.objects.filter(category__url_title="sport").order_by('-id')[:4],
            "local" : Article.objects.filter(category__url_title="local").order_by('-id')[:4],
            "science" : Article.objects.filter(category__url_title="science").order_by('-id')[:4],
            "travel" : Article.objects.filter(category__url_title="travel").order_by('-id')[:4],
            "health" : Article.objects.filter(category__url_title="health").order_by('-id')[:4],
            "style" : Article.objects.filter(category__url_title="style").order_by('-id')[:4],
            "weather" : Article.objects.filter(category__url_title="weather").order_by('-id')[:4],
            "gallery" : Article.objects.filter(category__url_title="gallery").order_by('-id')[:4],
        }
        return myset


class WorldListView(ListView):
    template_name = 'news/world.html'
    model = Article
    context_object_name = 'news'
    ordering = ['created_at']
    
    def get_queryset(self):
        return Article.objects.filter(category__url_title="world").order_by('-id')

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


def news_detail(request, news_id):
    news = Article.objects.get(id=news_id)
    comments = Comment.objects.filter(news=news)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            Comment.objects.create(news=news, author=author, content=content)
            return redirect('article_detail', news_id=news_id)
    else:
        form = CommentForm()

    return render(request, 'news/article.html', {'news': news, 'comments': comments, 'form': form})
