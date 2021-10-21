from view_crud.models import Student
from django.shortcuts import get_object_or_404
from view_crud.serializers import StudentSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response

class StudentViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        if pk is not None:
            queryset = Student.objects.get(pk=pk)
            serializer = StudentSerializers(queryset)
            return Response(serializer.data)

    def create(self, request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        queryset = Student.objects.get(pk=pk)
        serializer = StudentSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated!!'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Student.objects.get(pk=pk).delete()
        return Response({"msg":"Data Deleted"})
