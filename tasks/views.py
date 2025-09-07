from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .models import Task 
from .serializers import TaskSerializer 

class TaskViewSet(viewsets.ModelViewSet):
    """Provides list, create, retrieve, update, partial_update and destroy actions"""
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer