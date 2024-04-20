from django.shortcuts import render
from store.models import Category , Product
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse('<h1> Hello Django  </h1>')

def index(request):
    products=None
    products=Product.objects.all().filter(available=True)
    return render (request , 'index.html' ,{'products':products})





def product(request):
    return render (request , 'product.html')




# Create your views here.
