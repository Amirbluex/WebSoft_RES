from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from django.core.paginator import Paginator
from django.views.generic import TemplateView


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/blog_page.html", {'article': article})


def article_list(request):
    article = Article.objects.all()
    page_number = request.GET.get("page")
    paginator = Paginator(article, 3)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/blog_list.html", {'articles': object_list})


class TopbarPartialView(TemplateView):
    template_name = "includes/top_bar.html"

    def get_context_data(self, **kwargs):
        context = super(TopbarPartialView, self).get_context_data()
        context['category'] = Category.objects.all()
        return context


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, "blog/blog_list.html", {'articles': articles})


