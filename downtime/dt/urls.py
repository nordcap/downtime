from django.urls import path

from .views import CommentList, DownTimeListView, CommentDetail

urlpatterns = [
    path('work/<int:year>/<int:month>/<int:day>/', CommentList.as_view()),
    path('work/create/',CommentList.as_view()),
    path('work/<int:pk>/', CommentDetail.as_view()),
    # path('time/<int:year>/<int:month>/<int:day>/', DownTimeListView.as_view()),
]
