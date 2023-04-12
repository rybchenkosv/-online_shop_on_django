from django.shortcuts import render, get_object_or_404
from .models import Category, Products
from django.views import generic

def product_list(request, category_slug=None):
    category = None
    # СОЗДАЕМ ПЕРЕМЕННЫЕ ДЛЯ ОТОБРАЖЕНИЯ ВСЕХ ДАННЫХ, КОТОРЫЕ
    # МЫ ЗАПИХАЛИ В category,categories,post   И СОРТИРУЕМ ИХ ПО ДАТУ ПУБЛИКАЦИИ
    categories = Category.objects.all()
    products = Products.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    # РЕАЛИЗУЕМ ПЕРЕМЕННЫЕ ЧТОБЫ ПЕРЕДАТЬ ИХ В ШАБЛОН,
    # В ПОСЛЕДУЮЩЕМ ВСЕ ПЕРЕМЕННЫЕ МЫ СМОЖЕМ ТАК ЖЕ РЕАЛИЗОВЫВАТЬ И ПЕРЕДАВАТЬ В ШАБЛОН {{ post }} {{ category }} {{ categories }}
    return render(request,
                  'shop/shop_list.html',
                  {'category': category,
                   'categories': categories,
                   'post': products})

# Мы добавили шаблон для выносного элемента product_detail,
# который передает в представление параметры id и slug для извлечения конкретного продукта.
def post_detail(request, id, slug):
    post = get_object_or_404(Products,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/shop_list.html',
                  {'post': post})

# ДОБАВИЛ КЛАСС ДЛЯ ФИЛЬТРАЦИИ КАТЕГОРИЙ + ДОБАВИЛ HTML , НО ПОКА КАК ВСЕ СВЯЗАТЬ НЕ ПОНЯТНО
class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'shop/category_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['products'] = Products.objects.filter(category=self.object.id)
        return context