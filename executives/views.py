from django.shortcuts import render
from rest_framework.generics import ListAPIView
from executives.repositories import ExecutiveRepo
from executives.serializers import ExecutiveSerializer

# Create your views here.

exec_repo = ExecutiveRepo


class ExecutiveListView(ListAPIView):
    queryset = exec_repo.get_all_active()
    serializer_class = ExecutiveSerializer
