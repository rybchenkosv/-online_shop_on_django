from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')), # ПЕРЕНАПРАВЛЯЕМ ВСЕ ЗАПРОСЫ http://127.0.0.1:8000/ К shop.urls
                                    # И ТАМ НАХОДИМ ДАЛЬНЕЙШИЕ ИНСТРУКЦИИ
]
