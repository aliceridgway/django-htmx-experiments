from django.db import models

# Create your models here.


class ToDo(models.Model):
    class StatusChoice(models.TextChoices):
        TODO = "To Do"
        DOING = "Doing"
        DONE = "Done"

    name = models.CharField(max_length=255)
    status = models.CharField(
        choices=StatusChoice.choices, default=StatusChoice.TODO, max_length=255
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def complete(self):
        self.status = "done"
        self.save()
