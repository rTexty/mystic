from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import News, Category

def index (request):
    news = News.objects.order_by('category')
    context = {
    'news': news,
    'title': 'Список новостей',
    'category': Category.objects.all
    }
    return render(request, template_name='news/index.html', context= context)