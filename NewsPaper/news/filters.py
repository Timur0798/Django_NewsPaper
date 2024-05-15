from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='newsCategory',
        lookup_expr='exact',
        queryset=Category.objects.all(),
        label='Категория'
    )

    added_after = DateTimeFilter(
        field_name='creationTime',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}),
        label='Опубликована позднее:'
        )

    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'title': ['icontains']
       }