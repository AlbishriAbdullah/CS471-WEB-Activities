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

""" address1 = Address.objects.create(street='High Way',city='Dammam',postal_code='432123')
address2 = Address.objects.create(street='King Fahad St',city='Dammam',postal_code='65756')
address3 = Address.objects.create(street='main Street',city='Khobar',postal_code='56757')

student1 = Student.objects.create(name='Salman',age=24,address = address1)
student2 = Student.objects.create(name='Abdulrhman',age=23,address=address2)
student3 = Student.objects.create(name='Rayan',age=19,address=address3) """

# lab 8 task 7
def students_by_city(request):
    city_counts = (
        Student.objects.values('address__city')
        .annotate(student_count=Count('id'))    
        .order_by('address__city')            
    )
    
    return render(request, 'bookmodule/students_by_city.html', {'city_counts': city_counts})
# lab 5
def lab5_task1(request):
    return render(request, 'bookmodule/lab5_task1.html')

def lab5_task2(request):
    return render(request,'bookmodule/lab5_task2_3.html')

def lab5_task4(request):
    return render(request,'bookmodule/lab5_task4.html')

# lab 9 part 1
def list_books_lab9(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books_lab9.html', {'books' : books})

from django.http import HttpResponseRedirect

def addBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return HttpResponseRedirect('/books/list_books_lab9/')
    return render(request, 'bookmodule/addbook.html')

def editBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return HttpResponseRedirect('/books/list_books_lab9/')
    return render(request, 'bookmodule/editBook.html', {'book': book})

from django.shortcuts import get_list_or_404,get_object_or_404

def deleteBook(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect('/books/list_books_lab9/')
    return render(request, 'bookmodule/deleteBook.html',{'book' : book})

# lab 9 part 2
def list_books_form(request):
    books = Book.objects.all()  
    return render(request, 'bookmodule/list_books_lab9_part2.html', {'books': books})

from .forms import BookForm

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save()  
            return HttpResponseRedirect('/books/list_books_lab9_part2/')
    else:
        form = BookForm()  
    return render(request, 'bookmodule/add_book_lab9_part2.html', {'form': form})

def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)  
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book) 
        if form.is_valid():  
            form.save() 
            return HttpResponseRedirect('/books/list_books_lab9_part2/')
    else:
        form = BookForm(instance=book)  
    return render(request, 'bookmodule/edit_book_lab9_part2.html', {'form': form})

def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)  
    if request.method == 'POST':
        book.delete() 
        return HttpResponseRedirect('/books/list_books_lab9_part2/')
    return render(request, 'bookmodule/delete_book_lab9_part2.html', {'book': book})

# lab 10 task 1
from .models import Student

def list_students(request):
    students = Student.objects.all()  # Fetch all students from the database
    return render(request, 'bookmodule/list_students.html', {'students': students})


from .forms import StudentForm
from django.shortcuts import redirect

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():  
            form.save()  
            return redirect('students.list_students')  
    else:
        form = StudentForm()  
    return render(request, 'bookmodule/add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id) 
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():  
            form.save() 
            return redirect('students.list_students')  
    else:
        form = StudentForm(instance=student)  
    return render(request, 'bookmodule/edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)  
    if request.method == 'POST':  
        student.delete()
        return redirect('students.list_students')  
    return render(request, 'bookmodule/delete_student.html', {'student': student})


# lab 10 task 2
from .models import Student2
from .forms import Student2Form
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('students2.list_students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/add_student2.html', {'form': form})

def edit_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students2.list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/edit_student2.html', {'form': form})

def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('students2.list_students2')
    return render(request, 'bookmodule/delete_student2.html', {'student': student})


# lab 10 task 3
from .forms import ProductForm
from .models import Product

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'bookmodule/add_product.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'bookmodule/list_products.html', {'products': products})


