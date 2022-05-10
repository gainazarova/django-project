from rest_framework import generics

from project.models import Group, Students, Teacher
from project.serializers import GroupSerializer, GroupDetailSerializer, StudentSerializer, TeachersSerializer


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer

class StudentsListView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class TeachersListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer







