from django.urls import path

from .views import WorkDownTimeListView, WorkDownTimeDetailView, DownTimeListView

urlpatterns = [
    path('work/', WorkDownTimeListView.as_view()),
    path('work/<int:pk>/', WorkDownTimeDetailView.as_view()),
    path('time/', DownTimeListView.as_view()),
]
