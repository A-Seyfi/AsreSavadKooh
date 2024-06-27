from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def article(request):
    return render(request, "article.html")


def custom_404_page(request):
    return render(request, '404.html', status=404)


def signup(request):
    return render(request, "sign_up.html")

def signin(request):
    return render(request, "sign_in.html")

def forgot_pass(request):
    return render(request, "forgot.html")

def reset_pass(request):
    return render(request, "reset.html")