from django.shortcuts import render
from rest_framework.generics import ListAPIView  # Create your views here.
from examination_system.serializers import ExaminationScheduleSerializer
from examination_system.services import get_exam_schedules_service
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated


class GetExamSchedules(ListAPIView):
    serializer_class = ExaminationScheduleSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        service = get_exam_schedules_service
        status, context = service(request, self.serializer_class)
        return Response(status=status, data=context)
