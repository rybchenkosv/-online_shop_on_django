from django.shortcuts import render
from django.utils import timezone
from .models import Post

def shop_list(request):
    # СОЗДАЕМ ПЕРЕМЕННУЮ ДЛЯ ОТОБРАЖЕНИЯ ВСЕХ ДАННЫХ, КОТОРЫЕ МЫ ЗАПИХАЛИ В POST И СОРТИРУЕМ ИХ ПО ДАТУ ПУБЛИКАЦИИ
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # РЕАЛИЗУЕМ ПЕРЕМЕННУЮ posts ПОД НАЗВАНИЕМ 'posts' ЧТОБЫ ПЕРЕДАТЬ ЕЕ В ШАБЛОН,
    # В ПОСЛЕДУЮЩЕМ ВСЕ ПЕРЕМЕННЫЕ МЫ СМОЖЕМ ТАК ЖЕ РЕАЛИЗОВЫВАТЬ И ПЕРЕДАВАТЬ В ШАБЛОН {{ posts }}
    return render(request, 'shop/shop_list.html', {'posts': posts})
