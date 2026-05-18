# from django.shortcuts import render


from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
# Create your views here.
