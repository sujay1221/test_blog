import django_filters
from django_filters import DateFilter,CharFilter
from .models import blog


class BlogFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_posted',lookup_expr='gte')
    end_date = DateFilter(field_name='date_posted',lookup_expr='lte')
    title = CharFilter(field_name='title',lookup_expr='icontains')
    company_name = CharFilter(field_name='company_name',lookup_expr='icontains')

    class Meta:
        model = blog
        fields = '__all__'
        exclude = ['image1','image2','pdf','content']
