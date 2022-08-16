from django.urls import path

from product.views import CreateProductView, ListProductView, UpdateProductView, DeleteProducteView

urlpatterns = [
    path('create/product/', CreateProductView.as_view(), name="create_product"),
    path('list/product/', ListProductView.as_view(), name="list_product"),
    path('delete/product/<int:pk>/', DeleteProducteView.as_view(), name='delete_product'),
    path('update/product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),

]
