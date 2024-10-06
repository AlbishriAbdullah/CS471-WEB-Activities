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
]
