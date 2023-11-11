from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['USN', 'name', 'sex', 'DOB', 'email']  # Add other fields as needed
