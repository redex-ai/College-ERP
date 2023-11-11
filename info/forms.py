from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    email = forms.EmailField(max_length=254, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['email'].initial = self.instance.email

    def save(self, commit=True):
        self.instance.email = self.cleaned_data.get('email')
        return super().save(commit=commit)
