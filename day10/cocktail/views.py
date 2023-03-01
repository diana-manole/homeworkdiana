from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cocktail
from .forms import Cocktail_ListFORM

# Create your views here.


def index(request):
    return render(request, "cocktail/index.html")


@login_required
def cocktail(request):
    cocktail = Cocktail.objects.filter(author=request.user.id).order_by("name")
    mapper = {"cocktail": cocktail}
    return render(request, "cocktail/cocktail.html", mapper)

def cocktail_list(request):
    cocktail_list = Cocktail.objects.filter(author=request.user.id).order_by("name")
    mapper = {"cocktail_list": cocktail_list}
    return render(request, "cocktail/cocktail_list.html", mapper)


def addcocktail(request):
    if request.method != "POST":
        form = Cocktail_ListFORM()
    else:
        form = Cocktail_ListFORM(data=request.POST)

        """if form.is_valid:
            new_cat = form.save(commit=False)
            new_cat.author = request.user
            new_cat.save()
            return redirect("cocktail:cocktails")"""
    context = {"form": form}
    return render(request, "cocktail/newcocktail.html", context)
