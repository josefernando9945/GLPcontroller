from django import forms

from customer.models import Customer
from employee.models import Employee


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'street', 'number', 'district', 'city']

