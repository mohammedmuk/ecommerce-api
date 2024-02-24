from django.urls import path
from .views import Item

app_name = 'items'

urlpatterns = [
    path('', Item.as_view({'get' : 'list','post' : 'create'})),
    path('<int:pk>', Item.as_view({'get' : 'retrieve', 'patch' : 'partial_update'})),
]
