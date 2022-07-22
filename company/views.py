# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse, reverse_lazy
# from django.views.generic import RedirectView, CreateView, ListView
#
# from account.models import User
# from company.forms import CompanyForm
# from company.models import Company
#
#
# class CompanyAuthentication(LoginRequiredMixin, RedirectView):
#
#     def get_redirect_url(self, *args, **kwargs):
#         user = self.request.user
#         company_id = kwargs.get('company_id')
#         company = Company.objects.filter(id=company_id)
#         if user.is_superuser:
#             administrator = User.objects.filter(company=company)
#             if administrator.exists():
#                 self.request.session['company_id'] = company_id
#                 return reverse('home')
#         elif user.is_user:
#             if User.objects.filter(company=company).exists():
#                 self.request.session['company_id'] = company_id
#                 return reverse('home')
#         return reverse('home')
#
#
# class CreateCompanyView(CreateView):
#     model = Company
#     form_class = CompanyForm
#     template_name = 'company/company_create.html'
#     success_url = '/list/company/'
#
#     def get_success_url(self):
#         return reverse_lazy('home')
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         form.instance.user = self.request.user
#         form.instance.save()
#         self.request.session['company_id'] = form.instance.id
#         return response
#
#     def get_initial(self):
#         initial = super().get_initial()
#         if 'company' in self.request.GET:
#             company = Company.objects.get(id=self.request.GET.get('company', None))
#             initial.update({
#                 "company": company
#             })
#         return initial
#
#
#
# class ListCompanyView(ListView):
#     model = Company
#     form_class = CompanyForm
#     template_name = 'company/company_list.html'
#     success_url = '/list/company/'
#
