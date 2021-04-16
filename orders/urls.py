from django.urls import path
from .views import OrderView, OrderProductView

urlpatterns = [
    path('', OrderView.as_view({'get': 'list', 'post': 'create'})),
    path('', OrderProductView.as_view({'get': 'list', 'post': 'create'}))
]