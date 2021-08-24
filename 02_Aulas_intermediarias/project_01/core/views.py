from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name, age):
    return HttpResponse('<h1>Hello, Your name is {} and your age is {}</h1>'.format(name, age))

def calculator(request, operation, number1, number2):
    if operation == "sum":
        result = number1 + number2
        op = "+"
    elif operation == "sub":
        result = number1 - number2
        op = "-"
    elif operation == "mult":
        result = number1 * number2
        op = "x"
    elif operation == "div":
        result = number1 / number2
        op = "/"
    else:
        return HttpResponse("<h1>ERROR: This is not operator</h1>")

    return HttpResponse('<h1>Return:  {} {} {} = {} </h1>'.format(number1, op, number2, result))