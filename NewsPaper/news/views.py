from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from datetime import datetime
from .forms import PostForm
from django.urls import reverse_lazy

class PostsList(ListView):
    model = Post
    ordering = '-creationTime'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class NewsSearch(ListView):
    model=Post
    template_name = 'news_search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['time_now']=datetime.now()
        return context


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')