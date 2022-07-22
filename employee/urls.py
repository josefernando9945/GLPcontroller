from django.urls import path

from account.views import DeleteUserView, UpdateUserView
from employee.views import CreateEmployeeView, ListEmployeeView, DeleteEmployeeView, UpdateEmployeeView

urlpatterns = [
    path('create/employee/', CreateEmployeeView.as_view(), name="create_employee"),
    path('list/employee/', ListEmployeeView.as_view(), name="list_employee"),
    path('delete/employee/<int:pk>/', DeleteEmployeeView.as_view(), name='delete_employee'),
    path('update/employee/<int:pk>/', UpdateEmployeeView.as_view(), name='update_employee'),

]
