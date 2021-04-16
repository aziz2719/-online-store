from rest_framework import serializers
from .models import Order, OrderProduct

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('__all__')