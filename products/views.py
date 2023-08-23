from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .model import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ViewProduct(APIView):
    serializer_class = ProductSerializer

    @extend_schema(description="View to download course content.", responses={200: ProductSerializer})
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CreateProduct(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @method_decorator(login_required)
    @extend_schema(description="View to download course content.", responses={200: ProductSerializer})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product created successfully.'}, status=201)
        return Response(serializer.errors, status=400)


class UpdateProduct(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @method_decorator(login_required)
    @extend_schema(description="View to download course content.", responses={200: ProductSerializer})
    def post(self, request, product_id):
        product \
            = get_object_or_404(Product, pk=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated successfully.'})
        return Response(serializer.errors, status=400)


class DeleteProduct(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @method_decorator(login_required)
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
        return Response({'message': 'Product deleted successfully.'})


class ViewAllProducts(APIView):
    serializer_class = ProductSerializer

    @extend_schema(description="View to download course content.", responses={200: ProductSerializer})
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
