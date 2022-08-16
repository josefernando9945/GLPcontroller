
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('employee.urls')),
    path('', include('company.urls')),
    path('', include('customer.urls')),
    path('', include('product.urls')),
]
