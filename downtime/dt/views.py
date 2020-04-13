import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response

from rest_framework.views import APIView

from .models import WorkDownTime, DownTime
from .serializers import CommentSerializer, DownTimeSerializer


class CommentList(APIView):
    """вывод комментриев к работам производимым в определенный день"""

    def get(self, request, year=2020, month=1, day=1):
        print(request.data)
        search_date = datetime.date(year, month, day)
        queryset = WorkDownTime.objects.filter(date=search_date)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    """Извлечение, обновление и удалениое комментариев"""

    def get_object(self, pk):
        return get_object_or_404(WorkDownTime.objects.all(), pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class WorkDownTimeDetailView(APIView):
    """Комментарии к работе производимым для определенного объекта"""

    def get(self, request, pk):
        queryset = WorkDownTime.objects.get(id=pk)
        serializer = DownTimeSerializer(queryset)
        return Response(serializer.data)


class DownTimeListView(APIView):
    """Вывод данных по простоям за день"""

    def get(self, request, year, month, day):
        search_date = datetime.date(year, month, day)
        queryset = DownTime.objects.filter(date=search_date)
        serializer = DownTimeSerializer(queryset, many=True)
        return Response(serializer.data)
