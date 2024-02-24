from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from api.models import Item
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ItemSerializer


class Item(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_context(self):
        if self.action == 'partial_update':
            id = self.request.path.split('/')
            id = id[len(id) - 1]
            return {"user" : self.request.user, 'action' : self.action, "id" : int(id)}

        return {"user" : self.request.user, 'action' : self.action}