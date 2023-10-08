from django.urls import path

from .views import UploadFileView, ListOfFiles

urlpatterns = [
    path('upload/', UploadFileView.as_view()),
    path('files/', ListOfFiles.as_view()),
]
