import datetime

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Work, DownTime, TypeDownTime, ObjectDownTime
from .serializers import WorkSerializer, DownTimeSerializer


def index(request):
    return render(request, 'dt/index.html')


class DownTimeList(APIView):
    def get(self, request, year=2020, month=1, day=1):
        search_date = datetime.date(year, month, day)
        out = []
        queryset = DownTime.objects.filter(work__date=search_date)
        for t in list(queryset):
            res = {
                'date': t.work.date,
                'obj': t.work.obj.name,
                'comment1': t.work.comment_one,
                'comment2': t.work.comment_one,
                'type': t.type.name,
                'amount': t.amount,
                'smena': t.smena,
            }
            out.append(res)

        result = get_data_time(out)

        return Response(result)


# функция переформатирования вывода данных в вид удобный для использования во фронтэнде
def get_data_time(data_list):
    """получаем список уникальных объектов"""
    obj_name = []
    for obj_t in data_list:
        obj_name.append(obj_t["obj"])

    list_name_obj = list(set(obj_name))

    # получаем такую структуру
    result_list = []
    for name_obj in list_name_obj:
        dict_object = {
            'obj': name_obj,
            'smena1': {
                'types': [],
                'comment1': ''
            },
            'smena2': {
                'types': [],
                'comment2': ''
            }
        }
        result_list.append(dict_object)

    for item in data_list:
        for elem in result_list:
            if item["obj"] == elem["obj"]:
                elem["smena1"]["comment1"] = item["comment1"]
                elem["smena2"]["comment2"] = item["comment2"]
                if item["smena"] == "1":
                    elem["smena1"]["types"].append({
                        "type": item["type"],
                        "amount": item["amount"]
                    })
                if item["smena"] == "2":
                    elem["smena2"]["types"].append({
                        "type": item["type"],
                        "amount": item["amount"]
                    })

    return result_list


class WorkList(APIView):
    """вывод комментриев к работам производимым в определенный день"""

    def get(self, request, year=2020, month=1, day=1):
        search_date = datetime.date(year, month, day)
        queryset_works = Work.objects.filter(date=search_date)
        # for work in queryset_works:
        #     q_work = work.works.all()
        #     print(q_work)
        print(queryset_works)
        print(queryset_works[0].works.first().amount)
        serializer = WorkSerializer(queryset_works, many=True)
        return Response(serializer.data)

        # print(queryset_works.works.all())

    def post(self, request):
        serializer = WorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkDetail(APIView):
    """Извлечение, обновление и удалениое комментариев"""

    def get_object(self, pk):
        return get_object_or_404(Work.objects.all(), pk=pk)

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = WorkSerializer(comment)
        return Response(serializer.data)
