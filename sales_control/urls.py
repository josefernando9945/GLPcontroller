from django.urls import path

from sales_control.views import CreateSalesView, ListSalesView, DeleteSalesView, UpdateSalesView

urlpatterns = [
    path('create/sales/', CreateSalesView.as_view(), name="create_sales"),
    path('list/sales/', ListSalesView.as_view(), name="list_sales"),
    path('delete/sales/<int:pk>/', DeleteSalesView.as_view(), name='delete_sales'),
    path('update/sales/<int:pk>/', UpdateSalesView.as_view(), name='update_sales'),

]
