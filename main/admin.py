from django.contrib import admin
from .models import FreeServices
from .models import User
from .models import SiteOrder


admin.site.register(FreeServices)
admin.site.register(User)
admin.site.register(SiteOrder)