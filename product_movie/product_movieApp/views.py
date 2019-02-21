from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    databaseArray = Product.objects.all()
    print(databaseArray)
    return HttpResponse("Test A new URL")