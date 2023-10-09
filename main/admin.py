from django.contrib import admin
from .models import Task
from .models import FreeServices

admin.site.register(Task)
admin.site.register(FreeServices)