from django import forms

from sales_control.models import Sales


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = '__all__'

