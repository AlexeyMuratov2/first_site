from django.db import models


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


class SiteRequest(models.Model):
    site_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    urgently = models.BooleanField()
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.site_name
