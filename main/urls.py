from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('aboutus', views.about_us, name = 'about'),
    path('create_site', views.create_site, name = 'create'),
    path('order_list', views.order_list, name = 'orders'),
    path('update_order/<order_id>', views.update_order, name = 'update-order'),
    path('delete_order/<order_id>', views.delete_order, name = 'delete-order'),
    path('personal_account', views.personal_account, name = 'personal-account'),
]
