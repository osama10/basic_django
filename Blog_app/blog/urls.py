from django.contrib import admin
from django.urls import path,include
from .views import ArticleListView,ArticleDetailView,ArticleCreateView,ArticleUpdateView, ArticleDeleteView

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_list'),
    path('detail/<int:id>', ArticleDetailView.as_view(), name='article_detail'),
    path('create_article', ArticleCreateView.as_view(), name='article_create'),
    path('update_article/<int:id>', ArticleUpdateView.as_view(), name='article_update'),
    path('delete_article/<int:id>', ArticleDeleteView.as_view(), name='article_delete')

]
