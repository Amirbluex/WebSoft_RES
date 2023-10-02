from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name='blog_page'),
    path('list', views.article_list, name="blog_list"),
    path('topbar', views.TopbarPartialView.as_view(), name='topbar'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
]
