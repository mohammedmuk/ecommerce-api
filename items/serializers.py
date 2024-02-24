from rest_framework import serializers
from api.models import Item, Products
from products.serializers import ProductsSerializer
from api.models import Customers


class ItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all())
    product = serializers.SerializerMethodField()
    total_number = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'product_id', 'product','number','total_number', 'completed']


    def get_total_number(self, obj):
        return obj.number * obj.product_id.price
    
    def get_product(self, obj):
        product = obj.product_id
        serializer = ProductsSerializer(product)
        return serializer.data
    
    def validate(self, attrs):
        action = self.context.get('action')
        if action == 'partial_update':
            user = self.context.get('user')
            id = self.context.get('id')
            customer = Customers.objects.filter(order__id=id
                                            ,owner = user).exists()
            if customer:
               return attrs
            else:
               raise serializers.ValidationError('You have not the permission')
        return attrs