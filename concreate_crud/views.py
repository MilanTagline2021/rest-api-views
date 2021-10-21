from concreate_crud.models import Student
from concreate_crud.serializers import StudentSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class StudentsAPI(ListAPIView, CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentsAPI_PK(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
