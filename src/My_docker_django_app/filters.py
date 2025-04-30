import django_filters
from .models import DDSRecord, Status, Type, Category, Subcategories

class DDSRecordFilter(django_filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(field_name='date', label='Период дат')
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategories = django_filters.ModelChoiceFilter(queryset=Subcategories.objects.all())

    class Meta:
        model = DDSRecord
        fields = []