from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!" #add this line
    return render(request, "bookmodule/index.html" , {"name": name}) #your render line
    
def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))
