from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetView,
)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from account.forms import (
    CreateUserForm,
    UserForm,
    ChargePasswordForm,
    PasswordResetForm,
    PasswordConfirmForm,
    UserFormAdmin,
)

from account.models import User
from company.forms import CreateCompanyForm, CompanyForm
from company.models import Company


class LoginUserView(LoginView):
    template_name = "user/login.html"

    def get_success_url(self):
        company = Company.objects.filter(user=self.request.user).first()
        self.request.session["company_id"] = company.id
        return reverse_lazy("home")


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = "user/login.html"


class HomeUserView(LoginRequiredMixin, TemplateView):
    template_name = "user/dashboard.html"


def create_user_and_company(request):
    formcompany = CompanyForm()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        formcompany = CreateCompanyForm(request.POST)
        # monthly_plan = MonthlyPlan.objects.filter()

        if form.is_valid() and formcompany.is_valid():
            user = form.save()
            condo = formcompany.save()
            condo.user = user
            condo.save()

            # monthly_plan.create(
            #     value_monthly_plan=200,
            #     condo_id=condo.id,
            # )
            messages.success(request, "Seus dados foram salvos com sucesso!")
            return HttpResponseRedirect("/login")
        else:
            messages.error(request, "Ocorreu um erro no formulário abaixo!")

            return HttpResponseRedirect("/login")

    return render(
        request, "user/create.html", {"form": form, "formcompany": formcompany}
    )


class ListUserView(LoginRequiredMixin, ListView):
    template_name = "user/list.html"
    model = User
    paginate_by = 6

    def get_context_data(self, **kwargs):

        context = super(ListUserView, self).get_context_data(**kwargs)
        context["company"] = Company.objects.filter().first()

        return context


class UpdateUserView(LoginRequiredMixin, UpdateView):
    template_name = "user/update.html"
    model = User
    form_class = UserForm
    success_url = "/list/"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        r = super().form_valid(form)
        messages.success(self.request, "Seus dados foram salvos com sucesso!")
        return r

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro no formulário abaixo!")
        return super().form_invalid(form)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    template_name = "user/delete.html"
    model = User
    success_url = "/list/"

    def get_success_url(self):
        messages.success(self.request, "Seus dados foram excluidos com sucesso!")
        return super().get_success_url()


class ProfileUserView(LoginRequiredMixin, UpdateView):
    template_name = "user/profile.html"
    model = User
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(UpdateView):
    template_name = "password/password.html"
    model = User
    form_class = ChargePasswordForm
    success_url = reverse_lazy("login")

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user.username})
        return kwargs

    def form_valid(self, form):
        r = super(ChangePasswordView, self).form_valid(form)
        user = form.instance
        data = form.cleaned_data
        new_password = data.get("new_password", None)
        user.set_password(new_password)
        user.save()
        return r

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro no formulário abaixo!")
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user


class ResetPasswordView(PasswordResetView):
    template_name = "password/password_reset.html"
    model = User
    form_class = PasswordResetForm
    success_url = "/password-reset/done/"
    email_template_name = "password/password_reset_email.html"
    html_email_template_name = "password/password_reset_email.html"


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = "password/password_reset_done.html"
    success_url = "/password-reset/confirm/"


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = "password/password_reset_confirm.html"
    success_url = "/password-reset/complete/"
    form_class = PasswordConfirmForm


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = "password/password_reset_complete.html"


class UpdateUserAdministratorView(LoginRequiredMixin, UpdateView):
    template_name = "user/update_admin.html"
    model = User
    form_class = UserFormAdmin
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        r = super(UpdateUserAdministratorView, self).form_valid(form)
        user = form.instance
        data = form.cleaned_data
        new_password = data.get("new_password", None)
        user.set_password(new_password)
        user.save()
        messages.success(self.request, "Seus dados foram salvos com sucesso!")
        return r

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro no formulário abaixo!")
        return super().form_invalid(form)

class ProfileUserAdministratorView(UpdateView):
    template_name = "user/profile_admin.html"
    model = User
    form_class = UserFormAdmin
