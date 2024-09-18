# Task 6 
# apps/bookmodule/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), 
    path('index2/<int:val1>/', views.index2)
]

# apps/bookmodule/urls.py (last record on step 2 table)
from django.urls import path
urlpatterns = [
]

