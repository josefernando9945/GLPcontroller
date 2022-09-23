from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from sales_control.forms import SalesForm
from sales_control.models import Sales


class CreateSalesView(LoginRequiredMixin, CreateView):
    template_name = 'sales/sales_create.html'
    model = Sales
    form_class = SalesForm
    success_url = '/list/sales/'


class ListSalesView(LoginRequiredMixin, ListView):
    template_name = 'sales/sales_list.html'
    model = Sales
    form_class = SalesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sales.objects.filter()
        return context

    def get_queryset(self):
        result = super(ListSalesView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Sales.objects.filter(description__contains=query)

        return result


class UpdateSalesView(LoginRequiredMixin, UpdateView):
    template_name = 'sales/sales_update.html'
    model = Sales
    form_class = SalesForm
    success_url = '/list/sales/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales'] = Sales.objects.filter()
        return context

class DeleteSalesView(LoginRequiredMixin, DeleteView):
    template_name = 'sales/sales_delete.html'
    model = Sales
    success_url = '/list/sales/'

