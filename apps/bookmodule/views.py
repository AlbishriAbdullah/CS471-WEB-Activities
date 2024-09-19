from django.shortcuts import render
from django.shortcuts import render
def index(request):
    name = request.GET.get("name") or "world!" #add this line
    return render(request, "bookmodule/index.html" , {"name": name}) #your render line


def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))


def viewbook(request, bookId):
    # Assume that we have the following books somewhere (e.g., database)
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # 'book' is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)
