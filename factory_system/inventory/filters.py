import django_filters
from .models import board

class boardFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label="Search by Name"
    )

    class Meta:
        model = board
        fields = ['name']
