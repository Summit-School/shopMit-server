# ecommerce/urls.py

from django.urls import path
from . import Views

urlpatterns = [
    path('products/<int:product_id>/', Views.view_product, name='view_product'),
    path('products/create/', Views.create_product, name='create_product'),
    path('products/<int:product_id>/update/', Views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', Views.delete_product, name='delete_product'),
    path('products/all/', Views.view_all_products, name='view_all_products'),
    path('user/', Views.user_data, name='user_data'),
    path('forgot-password/', Views.forgot_password, name='forgot_password'),
    path('signup/', Views.signup, name='signup'),
    path('login/', Views.login, name='login'),
]
