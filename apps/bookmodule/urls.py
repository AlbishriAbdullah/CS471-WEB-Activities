from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/<int:val1>/', views.index2, name='index2'),  # Assuming you have an index2 view
    path('<int:bookId>', views.viewbook),
]
