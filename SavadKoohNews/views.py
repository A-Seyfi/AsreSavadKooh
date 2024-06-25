from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def article(request):
    return render(request, "article.html")


def custom_404_page(request):
    return render(request, '404.html', status=404)