from django.urls import path

from . import views

app_name = "catsapps"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("name/", views.name, name="names"),
    path("namesbycats/<int:name_id>", views.namesbycats, name="name"), 
    
    path("color/", views.color, name="colors"),
    path("colorbycats/<int:color_id>", views.colorbycats, name="color"), 
    
    path("cats/", views.cats, name="cats"),
    path("catss/<int:catss_id>", views.catss, name="cats"), 
]
 # "name/"- просто ссылка, views должен совпадать с нашей созданной функцией в ней, name="names"- как мы будем обращаться по ссылке в html