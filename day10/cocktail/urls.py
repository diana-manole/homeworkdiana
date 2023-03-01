from django.urls import path

from . import views

app_name = "cocktail"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("cocktail", views.cocktail, name="cocktails"),
    path("addcocktail", views.addcocktail, name="addcocktail"),
    path("listcocktail", views.cocktail_list, name="listcocktail"),
]
