from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.utils import timezone

# Create your views here.
def index(request):
    databaseArray = Product.objects.filter(quantity__lt = 2)
    print(databaseArray[0].quantity)
    databaseArray[0].quantity = 500
    databaseArray[0].save()
    return HttpResponse(databaseArray)

    # newObject = Product(name="Something Else", price=100, quantity = 5)
    # # newObject = Movie(name="something", starrating = 10, releaseDate = "")
    # newObject.save()
    #
    # databaseArray = Product.objects.all()
    # # print(databaseArray[0].name)
    # # print(databaseArray[0].quantity)
    #
    # return HttpResponse(databaseArray[0].name + " " + str(databaseArray[0].quantity))