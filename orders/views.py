from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from api.models import Orders
from .serializers import OrdersSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class Orders(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return self.queryset.filter(customer__owner = self.request.user, product__completed=False)
    
    def get_serializer_context(self):
        return {"action" : self.action, "user" : self.request.user}