from django.urls import path
from .views import *

app_name = 'your_app_name'  # Replace with your app name

urlpatterns = [
    path('view-product/<int:product_id>/', ViewProduct.as_view(), name='view-product'),
    path('create-product/', CreateProduct.as_view(), name='create-product'),
    path('update-product/<int:product_id>/', UpdateProduct.as_view(), name='update-product'),
    path('delete-product/<int:product_id>/', DeleteProduct.as_view(), name='delete-product'),
    path('view-all-products/', ViewAllProducts.as_view(), name='view-all-products'),
]
