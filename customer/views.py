from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from customer.forms import CustomerForm
from customer.models import Customer


class CreateCustomerView(LoginRequiredMixin, CreateView):
    template_name = 'customer/customer_create.html'
    model = Customer
    form_class = CustomerForm
    success_url = '/list/customer/'


class ListCustomerView(LoginRequiredMixin, ListView):
    template_name = 'customer/customer_list.html'
    model = Customer
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = Customer.objects.filter()
        return context

    def get_queryset(self):
        result = super(ListCustomerView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Customer.objects.filter(first_name__contains=query)

        return result


class UpdateCustomerView(LoginRequiredMixin, UpdateView):
    template_name = 'customer/customer_update.html'
    model = Customer
    form_class = CustomerForm
    success_url = '/list/customer/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = Customer.objects.filter()
        return context


class DeleteCustomerView(LoginRequiredMixin, DeleteView):
    template_name = 'customer/customer_delete.html'
    model = Customer
    success_url = '/list/customer/'






