from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('aboutus', views.about_us, name = 'about'),
    path('create_site', views.create_site, name = 'create'),
    path('order_list', views.order_list, name = 'orders'),
    path('my_orders/<order_id>', views.my_orders, name = 'my-orders'),
]
