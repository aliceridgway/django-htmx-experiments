from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

from core.forms import ToDoForm
from core.models import ToDo

PAGE_LIMIT = 15


def index(request: HttpRequest) -> HttpResponse:

    todos = ToDo.objects.all().order_by("-created")[:PAGE_LIMIT]

    context = {"todos": todos, "form": ToDoForm(), "Status": ToDo.StatusChoice}

    return render(request, "index.html", context)
