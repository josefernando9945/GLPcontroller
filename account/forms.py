import string

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.forms import forms, FileInput
from django import forms

from account.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email']




class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Senha',
                               strip=False,
                               help_text="please input password",
                               widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                 }))
    confirm_password = forms.CharField(label='Confirme a Senha',
                                       strip=False,
                                       help_text="please input password again",
                                       widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                         }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']


    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Senha não confere")
        # if len(password or ()) < 8:
        #     raise forms.ValidationError("Senha deve ter  mínimo de 8 caracteres")
        # if not any(x.isupper() for x in password):
        #     raise forms.ValidationError("Senha deve tem 1 letra maiúscula")
        # if not any(x.islower() for x in password):
        #     raise forms.ValidationError("Senha deve tem 1 letra minuscula")
        # if not any(x.isdigit() for x in password):
        #     raise forms.ValidationError("Senha deve ter minimo de 1 numero")

        # list = ['!', '"', '#', '%', '&', '-', '/', ':', ';', '<', '=', '>', '@', '_', '`', '{', '}', '~']
        # for data in list:
        #     standard = re.compile(data)
        #     search = standard.search(password)
        #     if search != None:
        #         characters = search.group()
        #         return characters
        #         busca.save()
        # else:
        #     raise forms.ValidationError("Senha deve ter minimo de 1 caractere especial")
        # return confirm_password

        # list = password
        # for n in string.punctuation:
        #     if n in password:
        #         return False
        # if n not in password:
        #     raise forms.ValidationError("Senha deve ter minimo de 1 caractere especial")

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=True)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


