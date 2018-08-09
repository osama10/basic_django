from django.shortcuts import render,get_object_or_404,reverse
from  .models import Article
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    template_name = 'blog/article_list_detail.html'
    queryset = Article.objects.all()

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'id': self.object.id})


class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse('blog:article_detail', kwargs={'id': self.object.id})

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_success_url(self):
        return reverse('blog:blog_list')

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)