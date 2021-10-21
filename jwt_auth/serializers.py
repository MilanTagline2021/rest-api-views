from rest_framework import serializers
from jwt_auth.models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']