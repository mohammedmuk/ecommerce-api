from rest_framework.viewsets import ModelViewSet
from api.models import Customers
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CustomersSerializer

# Create your views here.

class Customers(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
    def get_serializer_context(self):
        return {"user" : self.request.user, "username" : self.request.user.username}