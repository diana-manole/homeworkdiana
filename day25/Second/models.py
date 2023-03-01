from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=5, unique=True)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Woman(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self} "
