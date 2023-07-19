from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import category,product


# Create your views here.
# def index(request):
#     return HttpResponse("hey am inmakes ")


def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products=product.objects.all().filter(category=c_page,available=True)
    else:
        products=product.objects.all().filter(available=True)
    return render(request,"category.html",{'category':c_page,'products':products})
# Create your views here.

