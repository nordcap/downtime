from django.urls import path

from .views import WorkList, WorkDetail, DownTimeList

urlpatterns = [
    path('work/<int:year>/<int:month>/<int:day>/', WorkList.as_view()),
    path('work/create/', WorkList.as_view()),
    path('work/<int:pk>/', WorkDetail.as_view()),
    path('time/<int:year>/<int:month>/<int:day>/', DownTimeList.as_view())


    # path('time/<int:year>/<int:month>/<int:day>/', DownTimeListView.as_view()),
]
