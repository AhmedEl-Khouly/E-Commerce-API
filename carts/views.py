from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer, AddToCartSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class CartViewSet( CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        return Cart.objects.filter(user_id=self.request.user.id)
    


class CartItemViewSet(viewsets.ModelViewSet):
    # serializer_class = CartItemSerializer
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddToCartSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])



