from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
   # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    #allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod =Product.objects.filter(category=cat)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def ProductView(request):
    return HttpResponse("We are at product view")

def Checkout(request):
    return HttpResponse("We are at checkout")
def Register(request):
    return HttpResponse("We are at register")
def Login(request):
    return HttpResponse("we are at login")
def Cart(request):
    return HttpResponse("we are at Cart")
def Orders(request):
    return HttpResponse("we are at Orders")
def UserProfile(request):
    return HttpResponse("we are at Userprofile")
