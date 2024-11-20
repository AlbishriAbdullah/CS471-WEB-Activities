from django.shortcuts import render
from django.shortcuts import render
def index(request):
    name = request.GET.get("name") or "world!" #add this line
    return render(request, "bookmodule/index.html" , {"name": name}) #your render line


def index2(request, val1 = 0): #add the view function (index2)
    return HttpResponse("value1 = "+str(val1))


def viewbook1(request, bookId):
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

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
    
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True

            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

from .models import Book
from django.db.models import Q

# insert new data to the database using create function
mybook = Book.objects.create(title = 'Cybersecurity', author = 'Nelson', price = 20.4, edition = 2)
mybook2 = Book.objects.create(title = 'Medicine ', price = 90.99, author = 'M. Jackson', edition = 5)
mybook.save()

# to list all books in the database
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/booklist.html', {'books': books})

# task 3 lab 7
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

#task 4 lab 7
def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
# lab 8 task1
# bookmodule/views.py
def book_list_task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/book_list_task1.html', {'books': books})

def book_list_task2(request):
    books = Book.objects.filter(  Q(edition__gt=2) &  (Q(title__icontains='qu') | Q(author__icontains='qu')) )
    return render(request,'bookmodule/book_list_task2.html', {'books' : books})

def book_list_task3(request):
    books = Book.objects.filter(Q(edition__lte=2) & ~ (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request,'bookmodule/book_list_task3.html', {'books' : books})

def book_list_task4(request):
    books = Book.objects.order_by('title')
    return render(request,'bookmodule/book_list_task4.html',{'books' : books})

# lab 8 task 5
from django.db.models import Count, Sum, Avg, Max, Min
# lab 8 task 6
def book_statistics(request):
    # Aggregate data
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    
    return render(request, 'bookmodule/book_statistics.html', {'stats': stats})
# lab 8 task 6
from .models import Student, Address

address1 = Address.objects.create(street='High Way',city='Dammam',postal_code='432123')
address2 = Address.objects.create(street='King Fahad St',city='Dammam',postal_code='65756')
address3 = Address.objects.create(street='main Street',city='Khobar',postal_code='56757')

student1 = Student.objects.create(name='Salman',age=24,address = address1)
student2 = Student.objects.create(name='Abdulrhman',age=23,address=address2)
student3 = Student.objects.create(name='Rayan',age=19,address=address3)

# lab 8 task 9
def students_by_city(request):
    city_counts = (
        Student.objects.values('address__city')
        .annotate(student_count=Count('id'))    
        .order_by('address__city')            
    )
    
    return render(request, 'bookmodule/students_by_city.html', {'city_counts': city_counts})