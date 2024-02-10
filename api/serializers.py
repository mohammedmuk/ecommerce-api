from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = ['id', 'name', 'price']


class ItemSerializer(serializers.ModelSerializer):
    item = serializers.HyperlinkedRelatedField(
        view_name='api:item-detail',
        queryset=models.Products.objects.all()
    )
    total_number = serializers.SerializerMethodField()
    class Meta:
        model = models.Item
        fields = ['id', 'item', 'number','total_number', 'completed']

    def get_total_number(self, obj):
        return obj.number * obj.item.price



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CustomersSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    order = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Customers
        fields = ['id', 'owner' ,'order', 'total_price']

    def get_order(self, obj):
        user = self.context.get('user')
        orders = models.Orders.objects.filter(customer__owner=user, product__completed=True)
        li = []
        for order in orders:
            li.append(order.product)
        return ItemSerializer(li, many=True).data


    def get_total_price(self, obj):
        user = self.context.get('user')
        orders = models.Orders.objects.filter(customer__owner=user, product__completed=True)
        total_price = sum(order.product.number * order.product.item.price for order in orders)
        return total_price


class OrdersSerializer(serializers.ModelSerializer):
    customer = CustomersSerializer
    product = ItemSerializer

    class Meta:
        model = models.Orders
        fields = ['id', 'customer', 'product']



class InfoSerializer(serializers.ModelSerializer):
    owner = UserSerializer
    class Meta:
        model = models.Info
        fields = ['owner', 'first_name', 'last_name', 'phone', 'address','postal_code', 'state']

