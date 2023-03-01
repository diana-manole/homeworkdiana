from django import forms
from .models import Cocktail_List



class Cocktail_ListFORM(forms.ModelForm):
    class Meta:
        model = Cocktail_List
        fields = ["name", "recepe"]
        labels = {
            "name": "",
            "recepe": ""
        }



