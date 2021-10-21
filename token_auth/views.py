from token_auth.models import Student
from django.shortcuts import get_object_or_404
from token_auth.serializers import StudentSerializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]