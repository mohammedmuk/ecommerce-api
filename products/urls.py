from django.urls import path
from .views import Products


app_name = 'products'


urlpatterns = [
    path('', Products.as_view({'get' : 'list'}), name='products'),
    path('<int:pk>', Products.as_view({'get' : 'retrieve'})),
]
