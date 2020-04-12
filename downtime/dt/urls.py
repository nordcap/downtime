from django.urls import path

from .views import WorkDownTimeListView, WorkDownTimeDetailView, DownTimeListView

urlpatterns = [
    path('work/<int:year>/<int:month>/<int:day>/', WorkDownTimeListView.as_view()),
    path('work/<int:pk>/', WorkDownTimeDetailView.as_view()),
    path('time/<int:year>/<int:month>/<int:day>/', DownTimeListView.as_view()),
]
