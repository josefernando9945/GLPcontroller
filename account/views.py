from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, DeleteView, UpdateView

from account.forms import UserForm, CreateUserForm
from account.models import User
from controller.forms import CreateCompanyForm
from controller.models import Company


class LoginUserView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        if not Company.objects.filter(user=self.request.user).exists():
            return reverse_lazy('create')
        else:
            c = Company.objects.filter(user=self.request.user).first()
            self.request.session['company_id'] = c.id
            return reverse_lazy('home')


class LogoutUserView(LogoutView):
    template_name = 'login.html'


class HomeUserView(DetailView):
    template_name = 'dashboard.html'
    model = Company
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        if self.kwargs.get('pk'):
            user_id = self.kwargs.get('pk')
            return reverse_lazy('detail_owner')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return super(HomeUserView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs, user=self.request.user)
        context['company'] = Company.objects.filter(user=self.request.user)
#         context['residence'] = Apartment.objects.filter().first()
        company = Company.objects.filter(user=self.request.user)
        context['Company_name'] = Company.name
#         # billtopay_total = BillToPay.objects.filter().aggregate(Sum('value'))
#         # billtopay = BillToPay.objects.filter(status=False).aggregate(Sum('value'))
#         # account_paid = BillToPay.objects.filter(status=True).aggregate(Sum('value'))
#         # totalp1 = billtopay_total.get('value__sum')
#         # totalp2 = billtopay.get('value__sum')
#         # totalp3 = account_paid.get('value__sum')
#         # label = billtopay.get('label')
#         # context['billtopay_total'] = billtopay_total
#         # context['billtopay'] = billtopay
#         # context['account_paid'] = account_paid
#         # context['label'] = label
#         # billtoreceive_total = BillToReceive.objects.filter().aggregate(Sum('value'))
#         # billtoreceive = BillToReceive.objects.filter(status=False).aggregate(Sum('value'))
#         # account_received = BillToReceive.objects.filter(status=True).aggregate(Sum('value'))
#         # label = billtoreceive.get('label')
#         # totalr1 = billtoreceive_total.get('value__sum')
#         # totalr2 = billtoreceive.get('value__sum')
#         # totalr3 = account_received.get('value__sum')
#         # context['billtoreceive_total'] = billtoreceive_total
#         # context['billtoreceive'] = billtoreceive
#         # context['account_received'] = account_received
#         # if totalr3 != None:
#         #     total = totalr3 - totalp3
#         #     context['total'] = total
#         # else:
#         #     return context
#         # result = super(HomeUserView, self).get_queryset()
#         start_date = self.request.GET.get('start_date')
#         end_date = self.request.GET.get('end_date')
#         if start_date and end_date:
#             context = super().get_context_data(**kwargs)
#             context['condo'] = Condo.objects.filter().first()
#             context['residence'] = Apartment.objects.filter().first()
#             # conta = BillToPay.objects.filter(due_date__range=[start_date, end_date])
#             # context['billtopay_status'] = conta
#             # billtopay_total = BillToPay.objects.filter(
#             #                                            due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # billtopay = BillToPay.objects.filter(status=False,
#             #                                      due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # account_paid = BillToPay.objects.filter(status=True,
#             #                                         due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # totalp1 = billtopay_total.get('value__sum')
#             # totalp2 = billtopay.get('value__sum')
#             # totalp3 = account_paid.get('value__sum')
#             # label = billtopay.get('label')
#             # context['billtopay_total'] = billtopay_total
#             # context['billtopay'] = billtopay
#             # context['account_paid'] = account_paid
#             # context['label'] = label
#             # billtoreceive_total = BillToReceive.objects.filter(
#             #                                                    due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # billtoreceive = BillToReceive.objects.filter(status=False,
#             #                                              due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # account_received = BillToReceive.objects.filter(status=True,
#             #                                                 due_date__range=[start_date, end_date]).aggregate(
#             #     Sum('value'))
#             # label = billtoreceive.get('label')
#             # totalr1 = billtoreceive_total.get('value__sum')
#             # totalr2 = billtoreceive.get('value__sum')
#             # totalr3 = account_received.get('value__sum')
#             # context['billtoreceive_total'] = billtoreceive_total
#             # context['billtoreceive'] = billtoreceive
#             # context['account_received'] = account_received
#             # if totalr3 != None:
#             #     total = totalr3 - totalp3
#             #     context['total'] = total
#             # else:
#             #     return context
        return context


def create_user_and_company(request):
    formcompany = CreateCompanyForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        formcompany = CreateCompanyForm(request.POST)
        if form.is_valid() and formcompany.is_valid():
            user = form.save()
            company = formcompany.save()
            company.user = user
            company.save()

            return HttpResponseRedirect('/login')

    else:
        form = CreateUserForm()

    return render(request, 'create.html', {'form': form, 'formapartment': formcompany})


class ListUserView(ListView):
    template_name = 'list.html'
    model = User
    paginate_by = 6

    def get_context_data(self, **kwargs):

        context = super(ListUserView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.filter()
        # residence = Apartment.objects.filter().first()
        # context['residence'] = residence
        # conta = BillToPay.objects.filter()
        # context['billtopay_status'] = conta
        # billtopay = BillToPay.objects.filter().aggregate(Sum('value'))
        # total = billtopay.get('value__sum')
        # context['billtopay'] = billtopay
        # billtoreceive = BillToReceive.objects.filter().aggregate(Sum('value'))
        # total = billtoreceive.get('value__sum')
        # context['billtoreceive'] = billtoreceive
        # query = self.request.GET.get('q', '')
        # list_user = User.objects.filter(name__icontains=query) if query != '' else User.objects.all()
        # paginator = Paginator(list_user, self.paginate_by)
        #
        # page = self.request.GET.get('page', 1)
        #
        # try:
        #     page_obj = paginator.page(page)
        # except PageNotAnInteger:
        #     page_obj = paginator.page(1)
        # except EmptyPage:
        #     page_obj = paginator.page(paginator.num_pages)
        #
        # context['page_obj'] = page_obj
        # context['quant'] = list_user.count()
        # context['search'] = query
        return context

    # def get_queryset(self):
    #     result = super(ListUserView, self).get_queryset()
    #     query = self.request.GET.get('search')
    #     if query:
    #         product = User.objects.filter(first_name__contains=query)
    #         result = product
    #
    #     return result


class UpdateUserView(UpdateView):
    template_name = 'update.html'
    model = User
    form_class = UserForm
    success_url = '/list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = Company.objects.filter()
        return context






class DeleteUserView(DeleteView):
    template_name = 'delete.html'
    model = User
    success_url = '/list/'


# class DetailUserView(DetailView):
#     template_name = 'detail.html'
#     model = User
#     form_class = UserForm
#
#
# class ProfileUserView(UpdateView):
#     template_name = 'profile.html'
#     model = User
#     form_class = UserForm
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#
# class ChangePasswordView(UpdateView):
#     template_name = 'password/password.html'
#     model = User
#     form_class = ChargePasswordForm
#     success_url = reverse_lazy("login")
#
#     def get_form_kwargs(self):
#         kwargs = super(ChangePasswordView, self).get_form_kwargs()
#         kwargs.update({'user': self.request.user.username})
#         return kwargs
#
#
#     def form_valid(self, form):
#         r = super(ChangePasswordView, self).form_valid(form)
#         user = form.instance
#         data = form.cleaned_data
#         new_password = data.get('new_password', None)
#         user.set_password(new_password)
#         user.save()
#         return r
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#
# class ResetPasswordView(PasswordResetView):
#     template_name = 'password/password_reset.html'
#     model = User
#     form_class = PasswordResetForm
#     success_url = '/password-reset/done/'
#     email_template_name = "password/password_reset_email.html"
#     html_email_template_name = "password/password_reset_email.html"
#
#
# class ResetPasswordDoneView(PasswordResetDoneView):
#     template_name = 'password/password_reset_done.html'
#     success_url = '/password-reset/confirm/'
#
#
# class ResetPasswordConfirmView(PasswordResetConfirmView):
#     template_name = 'password/password_reset_confirm.html'
#     success_url = '/password-reset/complete/'
#     form_class = PasswordConfirmForm
#
#
# class ResetPasswordCompleteView(PasswordResetCompleteView):
#     template_name = 'password/password_reset_complete.html'
#
