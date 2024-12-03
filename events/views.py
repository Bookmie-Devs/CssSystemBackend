from django.shortcuts import render
from rest_framework.generics import ListAPIView
from events.repositories import EventRepo
from events.serializers import EventSerializer

# Create your views here.

event_repo = EventRepo


class EventListView(ListAPIView):
    queryset = event_repo.get_all_events()
    serializer_class = EventSerializer
