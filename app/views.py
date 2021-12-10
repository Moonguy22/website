from django.shortcuts import render
from django.http.response import HttpResponse

from app.models import Category, Product
# Create your views here.



def main(request):
    products = Product.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all().order_by('name')
    return render(request, 'main.html', {'categories':categories, 'products':products})

def detail(request, pk):
    categories = Category.objects.all().order_by('name') #чтоб появились названия всех категорий на стр дитейл
    product = Product.objects.get(pk=pk)
    return render(request, 'detail.html', {'categories':categories,'product':product})

