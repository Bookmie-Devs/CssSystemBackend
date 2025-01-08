from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.repository import ProductRepo
from products.serializers import ProductListSerializer

# Create your views here.


class ProductListView(ListAPIView):
    queryset = ProductRepo.get_all_products()
    serializer_class = ProductListSerializer
