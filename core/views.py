from django.shortcuts import render
from rest_framework import generics
from core.serializers import ContactUsSerializer
from core.models import ContactUs


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
