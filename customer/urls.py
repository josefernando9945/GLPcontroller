from django.urls import path

from customer.views import UpdateCustomerView, ListCustomerView, CreateCustomerView, DeleteCustomerView

urlpatterns = [
    path('create/customer/', CreateCustomerView.as_view(), name="create_customer"),
    path('list/customer/', ListCustomerView.as_view(), name="list_customer"),
    path('delete/customer/<int:pk>/', DeleteCustomerView.as_view(), name='delete_customer'),
    path('update/customer/<int:pk>/', UpdateCustomerView.as_view(), name='update_customer'),

]
