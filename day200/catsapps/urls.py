from django.urls import path

from . import views

app_name = "catsapps"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("names/", views.names, name="names"),
    path("names/<int:name_id>", views.name, name="name"),
    path("colors/", views.colors, name="colors"),
    path("colors/<int:color_id>", views.color, name="color"),
    path("catss/", views.catss, name="catss"),
    path("catss/<int:cats_id>", views.cats, name="cats"),
]
