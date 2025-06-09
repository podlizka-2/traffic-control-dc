from django.shortcuts import render

from django.views.generic.edit import CreateView
from .models import Transaction
from .forms import TransactionForm

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = '/'