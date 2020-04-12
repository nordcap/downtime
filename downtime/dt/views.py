import datetime

from django.shortcuts import render

from rest_framework.response import Response

from rest_framework.views import APIView

from .models import WorkDownTime, DownTime
from .serializers import WorkDownTimeSerializer, WorkDownTimeDetailSerializer, DownTimeSerializer


class WorkDownTimeListView(APIView):
    """вывод работ производимых в определенный день"""

    def get(self, request, year, month, day):
        search_date = datetime.date(year, month, day)
        queryset = WorkDownTime.objects.filter(date=search_date)
        serializer = WorkDownTimeSerializer(queryset, many=True)
        return Response(serializer.data)


class WorkDownTimeDetailView(APIView):
    """Комментарии к работе производимым для определенного объекта"""

    def get(self, request, pk):
        queryset = WorkDownTime.objects.get(id=pk)
        serializer = WorkDownTimeDetailSerializer(queryset)
        return Response(serializer.data)


class DownTimeListView(APIView):
    """Вывод данных по простоям за день"""

    def get(self, request, year, month, day):
        search_date = datetime.date(year, month, day)
        queryset = DownTime.objects.filter(date=search_date)
        serializer = DownTimeSerializer(queryset, many=True)
        return Response(serializer.data)
