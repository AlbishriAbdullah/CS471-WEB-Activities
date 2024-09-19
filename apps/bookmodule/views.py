from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    name = request.GET.get("name") or "world!" #add this line
    return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name


def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))