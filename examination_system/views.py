from django.shortcuts import render
from rest_framework.generics import ListAPIView  # Create your views here.
from examination_system.serializers import ExaminationScheduleSerializer


class GetExamSchedules(ListAPIView):
    serializer_class = ExaminationScheduleSerializer
