from django.contrib import admin
from .models import TransactionType, Category, SubCategory, Transaction

admin.site.register(TransactionType)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transaction)
