from django_filters import FilterSet, DateTimeFilter
from .models import Post
from django.forms import DateTimeInput

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Новость не ранее',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
       model = Post
       fields = {
           'title': ['icontains'],
           'postCategory__name': ['icontains']



       }