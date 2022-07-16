from django.urls import path

from arabic_writers.api import ArabicWriterAPIView, ArabicWriterDetailAPIView

urlpatterns = [
    # Arabic Writers
    path('arabic-writers/', ArabicWriterAPIView.as_view(),
         name='arabic-writer-list'),
    path('arabic-writers/<int:pk>/', ArabicWriterDetailAPIView.as_view(),
         name='arabic-writer-detail'),
]
