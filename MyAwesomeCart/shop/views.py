from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products =Product.objects.all()
    print(products)
    params={'product':'products'}
    return render(request,'shop/index.html',params)
def search(request):
    return HttpResponse("We are at search")
def productview(request):
    return HttpResponse("We are at product view")
def tracker(request):
    return HttpResponse("We are at tracker")
def checkout(request):
    return HttpResponse("We are at checkout")
def contact(request):
    return HttpResponse("We are at contact")
def about(request):
    return render(request,'shop/about.html')

