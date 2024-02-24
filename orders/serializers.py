from rest_framework import serializers
from api.models import Orders
from customers.serializers import CustomersSerializer 
from items.serializers import ItemSerializer
from api.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    customer = CustomersSerializer
    product = ItemSerializer

    class Meta:
        model = Orders
        fields = ['id', 'customer', 'product']

    def validate(self, data):
        action = self.context.get('action')
        user = self.context.get('user')
        if action == 'destroy':
            id = self.context.get('id')
            order = Orders.objects.filter(customer__owner=user, id=id).exists()
            if order:
                return data

        if str(user) == str(data['customer']):
            return data
        else:
            raise serializers.ValidationError('You have not the permission')




