from django import forms
from .models import DDSRecord 

class DDSRecordForm(forms.ModelForm):
    class Meta:
        model = DDSRecord
        fields = ['date', 'status', 'type', 'category', 'subcategories', 'total', 'comment']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


# Динамическая фильтрация категорий и подкатегорий.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategories'].queryset = Subcategories.objects.none()
        if 'type' in self.data and self.data['type'].isnumeric():
            type_id = int(self.data['type'])
            self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.type.category_set

        if 'category' in self.data and self.data['category'].isnumeric():
            category_id = int(self.data['category'])
            self.fields['subcategories'].queryset = Subcategories.objects.filter(category_id=category_id)
        elif self.instance.pk:
            self.fields['subcategories'].queryset = self.instance.category.subcategories_set


# Серверная валидация зависемостей между полями.
    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get('category')
        subcategory = cleaned_data.get('subcategory')
        type = cleaned_data.get('type')

        if category and type and category.type != type:
            raise forms.ValidationError("Выбранная категория не соответствует типу.")

        if subcategory and category and subcategory!= category:
            raise forms.ValidationError("Выбранная подкатегория не соответствует категории.")

        return cleaned_data





