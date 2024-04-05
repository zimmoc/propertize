from django.shortcuts import render
from finance.tasks import generate_rent_invoices
from django.http import HttpResponse
from .models import Transaction

# Create your views here.

def finance(request):
    generate_rent_invoices()
    return render(request, "finance/finance.html")

