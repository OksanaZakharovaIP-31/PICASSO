from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer
from .tasks import processed_file


class UploadFileView(APIView):
    """
    API эндпоинт upload/, который принимает POST-запросы для загрузки файлов.
    При загрузке файла создается объект модели File,
     сохраняется файл на сервере и запускается асинхронную задачу для обработки файла с использованием Celery.
     В ответ на успешную загрузку файла возвращается статус 201 и сериализованные данные файла.
     Иначе в ответ возвращется статус 400
    """

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            print('save')
            processed_file.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListOfFiles(generics.ListCreateAPIView):
    """
    API эндпоинт files/, возвращающий список всех файлов с их данными, включая статус обработки.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
