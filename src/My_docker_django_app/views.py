from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import DDSRecords, Status, Type, Category, Subcategories
from .forms import DDSRecordsForm
from .filters import DDSRecordFilter
from django.http import JsonResponse

# Create your views here.


class DDSRecordsListView(ListView):
    model = DDSRecords
    template_name = 'temlates/base.html'
    context_object_name = 'temlates'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = DDSRecordFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class DDSRecordsCreateView(CreateView):
    model = DDSRecords
    form_class = DDSRecordsForm
    template_name = 'temlates/dds_records_form.html'
    success_url = reverse_lazy('ddsrecord_list')

class DDSRecordsUpdateView(UpdateView):
    model = DDSRecords
    form_class = DDSRecordsForm
    template_name = 'temlates/dds_records_form.html'
    success_url = reverse_lazy('ddsrecord_list')

class DDSRecordsDeleteView(DeleteView):
    model = DDSRecords
    template_name = 'temlates/editing.html'
    success_url = reverse_lazy('ddsrecord_list')

def load_category(request):
    type_id = request.GET.get('type_id')
    category = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(category), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategories.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

