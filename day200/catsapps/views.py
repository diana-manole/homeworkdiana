from django.shortcuts import render, redirect
from .models import Name,Color,Cat
from .forms import NameForm,ColorForm,CatForm
# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "catsapps/index.html")

def name(request):
    name = Name.objects.all()
    content = {"NAME":name}
    return render(request, "catsapps/name.html", content)

def namesbycats(request, name_id):
    name = Cat.objects.filter(id=name_id)
    context = { "NAMESBYCATS": name}
    return render(request, "catsapps/namesbycats.html", context) 

def color(request):
    color = Color.objects.order_by("color")
    content = {"COLOR":color}
    return render(request, "catsapps/color.html", content)

def colorbycats(request, color_id):
    color = Cat.objects.filter(id=color_id)
    context = { "COLORBYCATS": color}
    return render(request, "catsapps/colorbycats.html", context) 

def cats(request):
    cats = Cat.objects.order_by("cats")
    context = {"CATS": cats}
    return render(request, "finapp/cats.html", context)

def catss(request, catss_id):
    catss = Cat.objects.filter(id=catss_id)
    context = { "CATSS": catss}
    return render(request, "catsapps/catss.html", context) 


