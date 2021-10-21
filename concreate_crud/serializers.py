from rest_framework import serializers
from concreate_crud.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']