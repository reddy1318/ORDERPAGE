from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from django.http import JsonResponse 
from .models import User, Address, Product, OrderList, Cart, CartItem, OrderTracking
from .serializers import UserSerializer, AddressSerializer, ProductSerializer,OrderListSerializer, CartSerializer, CartItemSerializer,OrderTrackingSerializer


@api_view(['POST'])
def create_user(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_address(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_product(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order_list(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = OrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_cart(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_cart(request, cart_id, *args, **kwargs):
    try:
        cart = Cart.objects.get(pk=cart_id)
        cart.delete()
        return JsonResponse({'message': 'Cart deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return JsonResponse({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({'error': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_cart_item(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order_tracking(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = OrderTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

