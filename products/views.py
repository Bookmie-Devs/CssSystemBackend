from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from products.repository import ProductRepo
from products.serializers import ProductListSerializer,ProductPaymentSerializer
from products.services import product_payment_service
# Create your views here.


class ProductListView(ListAPIView):
    queryset = ProductRepo.get_all_products()
    serializer_class = ProductListSerializer


class ProductPaymentView(CreateAPIView):
    serializer_class = ProductPaymentSerializer

    def post(self, request, *args, **kwargs):
        service = product_payment_service
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)
