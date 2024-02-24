from django.urls import path
from .views import Orders
urlpatterns = [
    path('', Orders.as_view({'get' : 'list', 'post' : 'create'})),
    path('<int:pk>', Orders.as_view({'delete' : 'destroy'})),
]
