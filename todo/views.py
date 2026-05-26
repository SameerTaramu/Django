# from django.shortcuts import render
# render() is used for html templates
# for eg: return render(request, "home.html")
# inside generics DRF gives you ready-made classes for common API tasks.
# serializer is used to convert python/django objects into JSON and vice versa
# class TodoListCreateView(generics.ListCreateAPIView): this means inside class we call generics.ListCreateAPIView 
# which combines both GET and POST features
# queryset tells DRF “Which data should this API work with?”
# Todo.objects.all() means Get all Todo objects from database like "SELECT * FROM todo";
# Serializer_class tells DRF “Use this serializer to convert data.”
# class TodoDetailView(generics.RetrieveUpdateDestroyAPIView): This handles operations for ONE specific todo item.
#  this also means we can apply methods like PUT/Patch/Delete/Get for one specific item 

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
