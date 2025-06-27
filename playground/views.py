from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def say_hello(request):
    return HttpResponse('hello world, finally, i make it')

def home(request):
    print("调用了 home 视图函数！")
    return render(request, 'home.html')

def new(request):
    return HttpResponse('new products')

def shangping(request):
    products = Product.objects.all()
    return render(request, 'shangping.html', {'products': products})



