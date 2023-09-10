from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.
# Request handler

def say_hello(request):

    # Pull data from db
    # Transform
    # Send Email

    # return HttpResponse('Hello World')
    query_set = Product.objects.all() 

    # for product in query_set:
    #     print(product)
    #    list(query_set)
    # query_set[0:5]


    return render(request, 'hello.html', {'name': 'Mosh'})




