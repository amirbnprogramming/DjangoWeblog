from django.urls import path, include
from rest_framework.routers import DefaultRouter


from articles import views

category_router = DefaultRouter()
article_router = DefaultRouter()
comment_router = DefaultRouter()

category_router.register('', views.CategoryListViewSet, basename='category_list')
article_router.register('', views.ArticleListViewSet, basename='article_list')
comment_router.register('', views.CommentListViewSet, basename='comment_list')



urlpatterns = [
    path('category/', include(category_router.urls)),
    path('article/', include(article_router.urls)),
    path('comment/', include(comment_router.urls)),
]