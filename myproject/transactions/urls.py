from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionCreateView.as_view(), name='transaction_create'),
]