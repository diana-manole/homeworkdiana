"# homeworkdiana" 
from django.shortcuts import render
from .models import Phone,Brand,Color
# Create your views here.


def index(request):
    """Home page of application"""
    return render(request, "finapp/index.html")

def stats(request):
    phone = Phone.objects.order_by("phone")
    context = {'phone': phone}
    return render(request,"finapp/allstats.html", context)

################################################################################
def phonewithbrand(request):
    l = Phone.objects.values('phone')
    s = []
    for i in l:
        s.append(i['brand'])
    s = set(s)    
    yy = []
    for y in s:
        yy.append(Brand.objects.get(id=y))
    yy.sort(key=lambda x: x.brand) 
    mapper = {'brand': yy}
    return render(request,"finapp/brandslist.html", mapper)


def phonewithcolor(request, year):

    m = Color.objects.filter(=color)
    months = []
    for income in m:
        months.append(income.month)
    months = set(months)
    months = list(months)
 
    mapper = {'MONTHS': months, "year_id": year}
    return render(request, "finapp/monthslist.html", mapper)
        

def ylist(request):
    years = Year.objects.order_by('year')
    mapper = {'YEARS': years}
    return render(request,"finapp/yearslist.html", mapper)


def incomes(request, year, month):
    incs = Incomes.objects.filter(year=year)
    incs = filter(lambda x: x.month.month==month, incs)
    mapper = {"INCOMES": incs}
    return render(request, "finapp/inclist.html", mapper)


    from django.shortcuts import render
from .models import Brand,Color,Phone
# Create your views here.

def index(request):
    """Home page of application"""
    return render(request, "finapp/index.html")

def stats(request):
    PHONES= Phone.objects.order_by("phones")
    context = {'phones': PHONES}
    return render(request,"finapp/allstats.html", context)

def brandlist(request):
    brand = Brand.objects.order_by('brand')
    mapper = {'BRAND': brand}
    return render(request,"finapp/brandslist.html", mapper)

def colorlist(request):
    color= Color.objects.order_by('color')
    mapper = {'COLOR': color}
    return render(request,"finapp/colorslist.html", mapper)

def phone(request, color , brand):
    phone= Phone.objects.filter(brand=brand)
    phone = filter(lambda x: x.color.color==color, phone)
    mapper = {"phone": phone}
    return render(request, "finapp/inclist.html", mapper)



