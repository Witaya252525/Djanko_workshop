from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.

# def index (request):
#     return HttpResponse (" Hello witaya Chaoson")

def index (request):
    return render (request ,"index.html")

def product (request):
    return render (request ,"product.html")

def witaya (request):
    return render (request ,"witaya.html")

# def about (request):
#     return HttpResponse (" This is about page")

