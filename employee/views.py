from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from employee.forms import EmployeeForm
from employee.models import Employee


class CreateEmployeeView(LoginRequiredMixin, CreateView):
    template_name = 'employee/employee_create.html'
    model = Employee
    form_class = EmployeeForm
    success_url = '/list/employee/'


class ListEmployeeView(LoginRequiredMixin, ListView):
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
        if query:
            result = Employee.objects.filter(first_name__contains=query)

        return result


class UpdateEmployeeView(LoginRequiredMixin, UpdateView):
    template_name = 'employee/employee_update.html'
    model = Employee
    form_class = EmployeeForm
    success_url = '/list/employee/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = Employee.objects.filter()
        return context

class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    template_name = 'employee/employee_delete.html'
    model = Employee
    success_url = '/list/employee/'



