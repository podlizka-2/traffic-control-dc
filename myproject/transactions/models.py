from django.db import models

# Create your models here.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Transaction(models.Model):
    type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = ChainedForeignKey(
        SubCategory,
        chained_field='category',
        chained_model_field='category',
        show_all=False,
        auto_choose=True,
        sort=True,
        null=True,
        blank=True,
        related_name='transactions'
    )