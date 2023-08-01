from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .model import Product


# Create your views here.
def view_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    data = {
        'name': product.name,
        'description': product.description,
        'price': str(product.price),
        'quantity': product.quantity,
    }
    return JsonResponse(data)

# Function to create a new product
@login_required
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product = Product.objects.create(name=name, description=description, price=price, quantity=quantity)
        return JsonResponse({'message': 'Product created successfully.'})
    else:
        return JsonResponse({'error': 'POST request required.'}, status=400)

# Function to update a product
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.save()
        return JsonResponse({'message': 'Product updated successfully.'})
    else:
        return JsonResponse({'error': 'POST request required.'}, status=400)

# Function to delete a product
@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return JsonResponse({'message': 'Product deleted successfully.'})

# Function to view all products
def view_all_products(request):
    products = Product.objects.all()
    data = [{'name': product.name, 'description': product.description, 'price': str(product.price), 'quantity': product.quantity} for product in products]
    return JsonResponse(data, safe=False)

# Function to read and update user data
