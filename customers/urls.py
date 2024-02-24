from django.urls import path
from .views import Customers

app_name = 'customers'

urlpatterns = [
    path('', Customers.as_view({'get' : 'list', 'post' : 'create'})),
    path('<int:pk>/', Customers.as_view({'patch' : 'partial_update', 'get' : 'retrieve'})),
]
