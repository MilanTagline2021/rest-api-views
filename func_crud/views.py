from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from func_crud.models import Student
from func_crud.serializers import StudentSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        snippets = Student.objects.all()
        serializer = StudentSerializers(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        snippet = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        id = Student.objects.get(pk=pk)
        if id is not None:
            serializer=StudentSerializers(id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        snippets = Student.objects.all()
        serializer = StudentSerializers(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    elif request.method == 'PUT':
        serializer = StudentSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_Accepted)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
