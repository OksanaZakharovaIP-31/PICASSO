from celery import shared_task
from .models import File


@shared_task
def processed_file(file_id: int):
    """
    Функция для обработки растровых изображений
    Передываемый пармаетр = id обрабатываемого файла
    """
    try:
        file = File.objects.get(id=file_id)
        file_name = file.file.name
        file_type = file_name.split('.')[-1]
        if file_type in ['png', 'jpg', 'git', 'raw', 'tiff', 'bmp', 'psd']:
            file.processed = True
    except File.DoesNotExist:
        pass
