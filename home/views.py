from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, "home/index.html", {'articles': articles})


# def article_list(request):
#     article = Article.objects.all()
#     return render(request, "home/index.html", {'article': article})
