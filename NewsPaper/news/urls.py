from django.urls import path
from .views import *

urlpatterns = [
   path('', PostsList.as_view(),name='posts_list'),
   path('<int:pk>', PostDetail.as_view(), name='new_detail'),
   path('news/search/', NewsSearch.as_view(), name='news_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/edit', NewsUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete', NewsDelete.as_view(),name='news_delete'),
   path('article/create/', ArticleCreate.as_view(), name='article_create'),
   path('article/<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
   path('article/<int:pk>/delete',ArticleDelete.as_view(),name='article_delete')
]