from django import forms
from .models import Book
from .models import Student

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition'] 

    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']  

from .models import Student2, Address2

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']  
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),  
        }


from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image']