from django.urls import path

from account.views import DeleteUserView, UpdateUserView
from company.views import ListCompanyView
from employee.views import CreateEmployeeView, ListEmployeeView

urlpatterns = [
    path('create/company/', CreateEmployeeView.as_view, name="create_company"),
    path('list/company/', ListCompanyView.as_view(), name="list_company"),
    path('delete/company/<int:pk>/', DeleteUserView.as_view(), name='delete_company'),
    path('update/company/<int:pk>/', UpdateUserView.as_view(), name='update_company'),

]
