from rest_framework import serializers
from items.serializers import ItemSerializer
from api.models import Customers, Orders
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class CustomersSerializer(serializers.ModelSerializer):
    owner = UserSerializer
    owner_details = serializers.SerializerMethodField()
    order = ItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    total_payment = serializers.SerializerMethodField()

    class Meta:
        model = Customers
        fields = ['id', 'owner','owner_details', 'order', 'total_price', 'total_payment']

    def get_order(self, obj):
        user = self.context.get('user')
        orders = Orders.objects.filter(customer__owner=user, product__completed=True)
        li = []
        for order in orders:
            li.append(order.product)
        return ItemSerializer(li, many=True).data
    
    def get_owner_details(self, obj):
        user = obj.owner
        serializer = UserSerializer(user)
        return serializer.data
    
    def get_total_price(self, obj):
        user = self.context.get('user')
        orders = Orders.objects.filter(customer__owner=user, product__completed=False)
        total_price = sum(order.product.number * order.product.product_id.price for order in orders)
        return total_price
    
    def get_total_payment(self, obj):
        user = self.context.get('user')
        orders = Orders.objects.filter(customer__owner=user, product__completed=True)
        total_price = sum(order.product.number * order.product.product_id.price for order in orders)
        return total_price