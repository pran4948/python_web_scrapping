from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    context = {
        "data" : 205119067,
        "section" : "odd"
    }
    return render(request,'index.html',context)

def submit(request):
    url = 'https://www.snapdeal.com/search?keyword='
    query = request.POST.get('pname')
    query = query.replace(' ','+')
    url+=query
    page = requests.get(url)
    soup = BeautifulSoup(page.content)

    #name = soup.find(class_='_4rR01T') #name
    name = soup.find(class_='product-title') #name
    #price = soup.find(class_='_1_WHN1') #price
    price = soup.find(class_='lfloat product-price') #price
    #reviews = soup.find(class_='_3LWZlK') #review points
    #reviews = soup.find(class_='rating-text') #review points
    reviews = soup.find(class_='product-rating-count')

    context = {
        'name':name.text,
        'price':price.text,
        'reviews':reviews.text,
    }
    print(url)
    return render(request,'submit.html',context)
