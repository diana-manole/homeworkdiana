from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Color(models.Model):
    color = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.color}"


class Behavor(models.Model):
    behavor = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f"{self.behavor}"


class Kind(models.Model):
    kind = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.kind}"


class Cat(models.Model):
    color = models.CharField(Color, max_length=30)
    behavor = models.CharField(Behavor, max_length=30)
    kind = models.CharField(Kind, max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f" Color: {self.color}, Behavior: {self.behavor},Kind: {self.kind}"
