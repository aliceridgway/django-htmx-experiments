from django.forms import ModelForm

from core.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ["name"]
