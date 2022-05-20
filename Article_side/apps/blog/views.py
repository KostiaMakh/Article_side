from django.shortcuts import render
from django.views.generic import ListView
from .models import Author, Article, Category, Organization


class MainPage(ListView):
    model = Article
    template_name = 'blog/index.html'


# Create your views here.
