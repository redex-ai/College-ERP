from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, required=True)

    class Meta:
        model = Student
        fields = '__all__'
