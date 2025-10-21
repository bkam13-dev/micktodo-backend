from django.shortcuts import render
from rest_framework import generics
from tasks.models import Task
from tasks.serializers import TaskSerializer

# Create your views here.

# vue de création d'une tâche et liste des tâches
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
# vue de modification complète ou spécifique d'une tâche et de suppression d'une tâche
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "slug"