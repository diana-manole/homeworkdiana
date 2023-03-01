from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Menu,Woman
from .forms import MenuFORM

# Create your views here.
def index(request):
    return render(request, "Second/index.html")

@login_required
def menu(request):
    menu = Menu.objects.filter(author=request.user.id).order_by("name")
    mapper = {"menu": menu}
    return render(request, "Second/menu.html", mapper)

def addmenu(request):
    if request.method != "POST":
        form = MenuFORM()
    else:
        form = MenuFORM(data=request.POST)

        """if form.is_valid:
            new_menu = form.save(commit=False)
            new_menu.author = request.user
            new_menu.save()
            return redirect("Second:menu")"""
    context = {"form": form}
    return render(request, "Second/newmenu.html", context)

def woman(request):
    woman = Woman.objects.filter(author=request.user.id)
    mapper = {"woman":woman}
    return render(request, "Second/woman.html", mapper)

"""
def words(request):
    words = Words.objects.filter(author=request.user.id).order_by("word")
    mapper = {"words": words}
    return render(request, "dict/words.html", mapper)


def addword(request):
    if request.method != "POST":
        form = WordFORM()
    else:
        form = WordFORM(data=request.POST)

        if form.is_valid:
            new_word = form.save(commit=False)
            new_word.author = request.user
            new_word.save()
            return redirect("dict:words")
    context = {"form": form}
    return render(request, "dict/newword.html", context)


def train(request):
    words = Words.objects.filter(author=request.user.id).order_by("?")[0:3]
    mapper = {"words": words}
    return render(request, "dict/train.html", mapper)
"""