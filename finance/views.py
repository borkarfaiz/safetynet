from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render

from .models import Employee


def index(request):
    return render(request, 'finance/index.html')


class CustomerView(ListView):
    template_name = 'finance/customer.html'
    context_object_name = 'employees_list'
    model = Employee


class TakenView(ListView):
    template_name = 'finance/taken.html'
    model = Employee


class GivenView(ListView):
    template_name = 'finance/given.html'
    model = Employee


class ProvidedView(ListView):
    template_name = 'finance/provided.html'
    model = Employee
