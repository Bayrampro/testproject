from django.contrib.auth.models import User
from django.db import models


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Ползователь')
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'