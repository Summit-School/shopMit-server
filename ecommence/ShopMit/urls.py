from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:product_id>/', views.view_product, name='view_product'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('products/all/', views.view_all_products, name='view_all_products'),
    path('user/', views.user_data, name='user_data'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]