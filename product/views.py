from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from product.forms import ProductForm
from product.models import Product


class CreateProductView(LoginRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    model = Product
    form_class = ProductForm
    success_url = '/list/product/'


class ListProductView(LoginRequiredMixin, ListView):
    template_name = 'product/product_list.html'
    model = Product
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter()
        return context

    def get_queryset(self):
        result = super(ListProductView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            result = Product.objects.filter(description__contains=query)

        return result


class UpdateProductView(LoginRequiredMixin, UpdateView):
    template_name = 'product/product_update.html'
    model = Product
    form_class = ProductForm
    success_url = '/list/product/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.filter()
        return context

class DeleteProducteView(LoginRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    success_url = '/list/product/'

