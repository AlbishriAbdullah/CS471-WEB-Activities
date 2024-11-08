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
]
