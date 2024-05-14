from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter
from datetime import datetime

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
