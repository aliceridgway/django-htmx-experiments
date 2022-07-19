from django import forms

from core.models import ToDo


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["name"]

    name = forms.CharField(
        label=False,
        widget=forms.TextInput(
            attrs={
                "aria-label": "name",
                "placeholder": "What do you need to do?",
                "class": "form-control form-control-lg inline-block",
            }
        ),
    )
