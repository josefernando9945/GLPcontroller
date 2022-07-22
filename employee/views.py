from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from employee.forms import EmployeeForm
from employee.models import Employee


class CreateEmployeeView(CreateView):
    template_name = 'employee/employee_create.html'
    model = Employee
    form_class = EmployeeForm
    success_url = '/list/employee/'


class ListEmployeeView(ListView):
    template_name = 'employee/employee_list.html'
    model = Employee
    form_class = EmployeeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.filter()
        return context

    def get_queryset(self):
        result = super(ListEmployeeView, self).get_queryset()
        query = self.request.GET.get('search')

        return result


class UpdateEmployeeView(UpdateView):
    template_name = 'employee/employee_update.html'
    model = Employee
    form_class = EmployeeForm
    success_url = '/list/employee/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.filter()
        return context

class DeleteEmployeeView(DeleteView):
    template_name = 'employee/employee_delete.html'
    model = Employee
    success_url = '/list/employee/'



