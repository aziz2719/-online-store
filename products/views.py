from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .models import ProductMark
from .serializers import ProductSerializer
from .serializers import ProductMarkSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView, Response
from .permissions import IsProductUserOrReadOnly, IsCommentsOwnerOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from .service import ProductFilter


class ProductsView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsProductUserOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = ProductFilter

class ProductMarkView(ModelViewSet):
    queryset = ProductMark.objects.all()
    serializer_class = ProductMarkSerializer
    permission_classes = (IsCommentsOwnerOrReadOnly, )
    lookup_field = 'pk'
