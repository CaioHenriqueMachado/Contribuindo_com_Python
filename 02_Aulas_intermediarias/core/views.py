from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, age):
    return HttpResponse('<h1>Hello {} de {} </h1>'.format(name, age))
