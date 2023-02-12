from django import forms
from .models import Name, Color, Cat


class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name']
        labels = {'name': ''}
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ["color"]
        labels = {"Color": ""}
               
        
class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ["color","name"]
        labels = {"color": "color","name": "name"}
        
        