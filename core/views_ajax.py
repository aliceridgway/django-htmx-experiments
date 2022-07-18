from django import forms
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest

from django.shortcuts import render, get_object_or_404

from core.models import ToDo

from . import forms


def add_todo(request: HttpRequest) -> HttpResponse:

    form = forms.ToDoForm(request.POST)

    if not form.is_valid():
        return HttpResponseBadRequest()

    todo = form.save()

    context = {"todo": todo}

    return render(request, "partials/todo_row.html", context)


def complete(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(ToDo, pk=pk)

    todo.complete()

    context = {"todo": todo}

    return render(request, "partials/todo_row.html", context)


def delete(request: HttpRequest, pk: int) -> HttpResponse:
    todo = get_object_or_404(ToDo, pk=pk)

    todo.delete()

    return HttpResponse("<tr></tr>")


def filter_list(request: HttpRequest, status: str) -> HttpResponse:

    todos = ToDo.objects.filter(status=status)

    context = {"todos": todos, "Status": ToDo.StatusChoice}

    return render(request, "partials/todo_list.html", context)


def get_all_todos(request: HttpRequest) -> HttpResponse:

    todos = ToDo.objects.all()

    context = {"todos": todos, "Status": ToDo.StatusChoice}

    return render(request, "partials/todo_list.html", context)
