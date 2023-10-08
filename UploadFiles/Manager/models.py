from django.db import models

# Create your models here.


class File(models.Model):
    """
    file: поле типа FileField, используемое для загрузки файла.
    uploaded_at: поле типа DateTimeField, содержащее дату и время загрузки файла.
    processed: поле типа BooleanField, указывающее, был ли файл обработан.
    """
    file = models.FileField(),
    upload_at = models.DateTimeField(auto_now=True)
    processed = models.BooleanField(default=False)