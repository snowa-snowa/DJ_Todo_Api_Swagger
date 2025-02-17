from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Todo
from django.views.decorators.http import require_http_methods
from .serializers import TodoSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filter


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list": todos})


@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    description = request.POST['description']
    todo = Todo(title=title, description=description)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")


class Todos(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = "__all__"
    filterset_fields  = "__all__"
    search_fields = "__all__"
    # filterset_class = ProductFilter

"""
"filterset_fields" и "filterset_class" конфликтуют между собой и не могут вместе работать
"""
