from django.db import models
from django.contrib.auth.models import User

class Cocktail(models.Model):
    name = models.CharField(max_length=30, unique=True)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Cocktail_List(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    name = models.TextField()
    recepe = models.TextField(max_length=50)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.cocktail} : {self.recepe}"
