from django import forms
from .models import Menu


class MenuFORM(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name"]
        labels = {"name": "Название категории"}


