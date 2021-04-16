from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer
from rest_framework.permissions import IsAuthenticated



class OrderView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, ) 


class OrderProductView(ModelViewSet):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

""" def total_price_of_goods(self, price, total_price, product):
        if self.product > 1:
            self.total_price = self.price + self.price
            print(self.total_price)"""