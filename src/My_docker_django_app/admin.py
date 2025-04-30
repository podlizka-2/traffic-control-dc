# records/admin.py
from django.contrib import admin
from .models import Status, Type, Category, Subcategories, DDSRecords

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategories)
admin.site.register(DDSRecords)