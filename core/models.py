from django.db import models

# Create your models here.


class ToDo(models.Model):

    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("doing", "Doing"),
        ("done", "Done"),
        ("abandoned", "Abandoned"),
    ]

    name = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, default="todo", max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
