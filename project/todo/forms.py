from django import forms

from .models import ToDo


class NewItemForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = {"name": None}


class UpdateItemForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = {"name": None, "done": None}
