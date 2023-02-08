from django.shortcuts import render
from .models import Name,Color,Cat

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "catsapps/index.html")

def name(request):
    name = Name.objects.order_by("name")
    content = {"name":name}
    return render(request, "catsapps/name.html", content)

def names(request, name_id):
    name = Name.objects.get(id=name_id)
    cats = name.entry_set.order_by("cats")
    context = { "name": name, "cats": cats}
    return render(request, "catsapps/name.html", context)


def color(request):
    color = Color.objects.order_by("color")
    content = {"color":color}
    return render(request, "catsapps/color.html", content)

def colors(request, color_id):
    color = Color.objects.get(id=color_id)
    cats = color.entry_set.order_by("color")
    context = {"color": color, "cats": cats}
    return render(request, "firstapps/color.html", context)



def cats(request):
    cats = Cat.objects.order_by("cats")
    context = {"cats": cats}
    return render(request, "finapp/cats.html", context)

def catss(request, cats_id):
    catss = Cat.objects.get(id=cats_id)
    cats = catss.entry_set.order_by("cats")
    context = {"cats": cats, "catss": catss}
    return render(request, "firstapps/cats.html", context)


