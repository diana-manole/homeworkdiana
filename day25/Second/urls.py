from django.urls import path

from . import views

app_name = "Second"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("menu", views.menu, name="menus"),
    path("addmenu", views.addmenu, name="addmenu"),
    path("woman", views.woman, name="woman"),
]
