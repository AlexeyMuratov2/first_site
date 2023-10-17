from django.db import models
from django.conf import settings


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


class User(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name + ' ' + self.surname


class SiteOrder(models.Model):
    site_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    urgently = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.site_name
