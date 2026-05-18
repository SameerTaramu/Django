from django.urls import path
from .views import TodoListCreateView, TodoDetailView


urlpatterns = [
    path('todos/', TodoListCreateView.as_view()),
    # It converts a class-based view into a callable view function that Django can use in urls.py.
    path('todos/<int:pk>/', TodoDetailView.as_view()),

    ]