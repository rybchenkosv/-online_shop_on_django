from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_list, name='shop_list'), #views.post_list, name='post_list'
]
