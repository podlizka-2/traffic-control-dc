import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from transactions.models import TransactionType, Category, SubCategory

# Добавление типов транзакций:
types = ['Списание', 'Пополнение']
for t in types:
    obj, created = TransactionType.objects.get_or_create(name=t)
    if created:
        print(f"Добавлен тип: {t}")

# Добавление категорий:
categories = ['Инфраструктура', 'Маркетинг']
for c in categories:
    cat_obj, created = Category.objects.get_or_create(name=c)
    if created:
        print(f"Добавлена категория: {c}")

# Добавление подкатегорий:
subcategories_data = {
    'Инфраструктура': ['VPS', 'PROXY'],
    'Маркетинг': ['Avito', 'FARPOST']
}

for cat_name, subcats in subcategories_data.items():
    category_obj = Category.objects.get(name=cat_name)
    for sub in subcats:
        sub_obj, created = SubCategory.objects.get_or_create(name=sub, category=category_obj)
        if created:
            print(f"Добавлена подкатегория: {sub} к категории {cat_name}")