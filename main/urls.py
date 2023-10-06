from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('aboutus', views.about_us, name = 'about'),
    path('crate', views.create, name = 'create')
]
