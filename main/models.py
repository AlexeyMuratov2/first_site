from django.db import models

class Task(models.Model):
    title = models.CharField('название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class FreeServices(models.Model):
    case1 = models.CharField(max_length=150)
    case2 = models.CharField(max_length=150)
    case3 = models.CharField(max_length=150)
    case4 = models.CharField(max_length=150)

    def __str__(self):
        return self.case1

    class Meta:
        verbose_name = 'бесплатные услуги'
        verbose_name_plural = 'бесплатные услуги'