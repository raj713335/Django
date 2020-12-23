# articles/views.py

from django.views.generic import ListView
from .models import Article

from django.shortcuts import render

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'