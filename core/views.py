from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

from core.forms import ToDoForm
from core.models import ToDo

PAGE_LIMIT = 15


def index(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()

    todos = ToDo.objects.all().order_by("-created")[:PAGE_LIMIT]

    context = {"todos": todos, "form": ToDoForm()}

    return render(request, "index.html", context)
