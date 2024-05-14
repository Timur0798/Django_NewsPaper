from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter
from django.forms import DateTimeInput
from .models import Post, Category


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='added_at',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ))
    category=ModelMultipleChoiceFilter(
        field_name='categoryType',
        lookup_expr='exact',
        queryset=Category.objects.all(),
        label='Категория'
    )
    class Meta:
       model = Post
       fields = {
           # поиск по названию
           'title': ['icontains']
       }