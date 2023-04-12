from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.product_list,
         name='shop_list'),
    path('',
        views.product_list,
        name='shop_list_by_category'),
    path('',
        views.post_detail,
        name='shop_detail'),
]

