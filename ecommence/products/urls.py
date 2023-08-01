from django.urls import path
from . import views
urlpatterns = [
    path('products/<int:product_id>/', views.view_product, name='view_product'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('products/all/', views.view_all_products, name='view_all_products'),
    ]