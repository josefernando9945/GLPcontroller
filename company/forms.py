from django import forms
from django.forms import FileInput

from controller.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'autofocus': True
            }),
            'picture': FileInput(attrs={
                'class': 'custom-file-input',
                'placeholder': 'Foto',
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Endereço',
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numero',
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade',
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Estado',
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cep',
            }),

        }


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome Da Empresa',
        }),


    }
