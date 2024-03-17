from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from articles.models import Article, Category, Comment
from articles.serializer import CategorySerializer, ArticleSerializer, CommentSerializer


class HomePageView(TemplateView):
    template_name = 'index.html'


# Create your views here.
class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.get_all_objects()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class ArticleListViewSet(viewsets.ModelViewSet):
    queryset = Article.get_all_objects()
    serializer_class = ArticleSerializer
    pagination_class = PageNumberPagination


class CommentListViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
