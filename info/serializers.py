from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['USN', 'name', 'class_id', 'sex', 'DOB', 'email']  # Add 'email' to the fields list
