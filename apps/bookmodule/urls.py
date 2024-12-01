from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/<int:val1>/', views.index2, name='index2'),  # Assuming you have an index2 view
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"), #
    path('list_books/', views.list_books, name= "books.list_books"), #
    path('<int:bookId>/', views.viewbook, name="books.one_book"), # here i think we must check the name
    path('aboutus/', views.aboutus, name="books.aboutus"), #
    path('search/',views.search, name='books.search'),
    path('booklist/', views.book_list, name='book_list'),
    path('query/',views.simple_query,name='books.query'), # task 3
    path('complexQuery/',views.complex_query,name='books.complexQuery'),
    path('book_list_task1/',views.book_list_task1,name='books.book_list_task1'),
    path('book_list_task2/',views.book_list_task2,name='books.book_list_task2'),
    path('book_list_task3/',views.book_list_task3,name='books.book_list_task3'),
    path('book_list_task4/',views.book_list_task4,name='books.book_list_task4'),
    path('book_statistics/',views.book_statistics,name='books.book_statistics'),
    path('students_by_city/',views.students_by_city, name='books.students_by_city'),
    path('lab5_task1/', views.lab5_task1, name='books.lab5_task1'),
    path('lab5_task2_3/',views.lab5_task2,name='books.lab5_taks2_3'),
    path('lab5_task4/',views.lab5_task4,name='books.lab5_task4'),
    path('list_books_lab9/',views.list_books_lab9,name='books.list_books_lab9'),
    path('addBook/',views.addBook,name='books.addBook'),
    path('editBook/<int:id>/',views.editBook,name='books.editBook'),
    path('deleteBook/<int:id>/',views.deleteBook,name='books.deleteBook'),
    path('list_books_lab9_part2/', views.list_books_form, name='books.list_books_lab9_part2'),  
    path('add_book_lab9_part2/', views.add_book_form, name='books.add_book_part2'), 
    path('edit_book_lab9_part2/<int:id>/', views.edit_book_form, name='books.edit_book_part2'),  
    path('delete_book_lab9_part2/<int:id>/', views.delete_book_form, name='books.delete_book_part2'), 

    path('students_lab10/', views.list_students, name='students.list_students'),
    path('add_student_lab10/', views.add_student, name='students.add_student'),  # Add student
    path('edit_student_lab10/<int:id>/', views.edit_student, name='students.edit_student'),  # Edit student
    path('delete_student_lab10/<int:id>/', views.delete_student, name='students.delete_student'),  # Delete student

    
    path('students2/', views.list_students2, name='students2.list_students2'),
    path('add_student2/', views.add_student2, name='students2.add_student2'),
    path('edit_student2/<int:id>/', views.edit_student2, name='students2.edit_student2'),
    path('delete_student2/<int:id>/', views.delete_student2, name='students2.delete_student2'),

    path('products/', views.list_products, name='list_products'),  
    path('add_product/', views.add_product, name='add_product'), 


]
