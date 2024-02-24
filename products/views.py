from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from api.models import Products
from .serializers import ProductsSerializer

# Create your views here.

class Products(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    renderer_classes = [JSONRenderer]
