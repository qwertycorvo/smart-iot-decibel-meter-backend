from django.urls import path
from .views import ReadingListAPIView, ReadingLatestAPIView

urlpatterns = [
    path('readings/', ReadingListAPIView.as_view(), name='reading-list'),
    path('readings/latest/', ReadingLatestAPIView.as_view(), name='reading-latest'),
]