from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['USN', 'name', 'class_id', 'sex', 'DOB', 'email']  # Add other fields as needed
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }
